import { Component, OnInit, CUSTOM_ELEMENTS_SCHEMA } from '@angular/core';
import { ActivatedRoute } from '@angular/router';
import { HttpClient, HttpHeaders } from '@angular/common/http';
import { CommonModule } from '@angular/common';
import { FormsModule } from '@angular/forms';
import { NzCardModule } from 'ng-zorro-antd/card';
import { NzRateModule } from 'ng-zorro-antd/rate';
import { NzCarouselModule } from 'ng-zorro-antd/carousel';
import { NzImageModule } from 'ng-zorro-antd/image';
import { NzButtonModule } from 'ng-zorro-antd/button';
import { NzDividerModule } from 'ng-zorro-antd/divider';
import { NzDescriptionsModule } from 'ng-zorro-antd/descriptions';
import { NzSpinModule } from 'ng-zorro-antd/spin';
import { NzAlertModule } from 'ng-zorro-antd/alert';
import { NzGridModule } from 'ng-zorro-antd/grid';
import { NzModalModule } from 'ng-zorro-antd/modal';
import { NzInputModule } from 'ng-zorro-antd/input';
import { NzMessageModule, NzMessageService } from 'ng-zorro-antd/message';
import { AuthService } from '../auth.service';
import { NzPopconfirmModule } from 'ng-zorro-antd/popconfirm';

/**
 * DetailsComponent is the component for displaying the details of a specific hotel.
 */
@Component({
  selector: 'app-details',
  templateUrl: './details.component.html',
  styleUrls: ['./details.component.css'],
  standalone: true,
  imports: [
    CommonModule,
    FormsModule,
    NzCardModule,
    NzRateModule,
    NzCarouselModule,
    NzImageModule,
    NzButtonModule,
    NzDividerModule,
    NzDescriptionsModule,
    NzSpinModule,
    NzAlertModule,
    NzGridModule,
    NzModalModule,
    NzInputModule,
    NzMessageModule,
    NzPopconfirmModule
  ],
  schemas: [CUSTOM_ELEMENTS_SCHEMA]
})
export class DetailsComponent implements OnInit {
  hotelId: string | null = null;
  Details: any = null;
  Comments: any[] = [];
  AddComment: any = { content: '', rating: null };
  DeleteId: string = '';
  carouselEffect = 'scrollx';
  
  isModalVisible = false;
  isLoggedIn = false;
  isLoginModalVisible = false;
  modalTitle = 'Add Comment';
  editingCommentId: string | null = null;
  loginForm = {
    username: '',
    password: ''
  };

  /**
   * Constructor to initialize the DetailsComponent.
   * @param route - ActivatedRoute to get route parameters.
   * @param http - HttpClient to make HTTP requests.
   * @param authService - AuthService to handle authentication.
   * @param message - NzMessageService to display messages.
   */
  constructor(
    private route: ActivatedRoute,
    private http: HttpClient,
    private authService: AuthService,
    private message: NzMessageService
  ) {
    this.authService.isLoggedIn$.subscribe(
      status => this.isLoggedIn = status
    );
  }

  /**
   * Lifecycle hook that is called after data-bound properties of a directive are initialized.
   */
  ngOnInit() {
    this.hotelId = this.route.snapshot.paramMap.get('id');
    if (this.hotelId) {
      this.fetchHotelDetails(this.hotelId);
      this.fetchComments(this.hotelId);
    }
  }

  /**
   * Fetches the details of the hotel from the server.
   * @param id - The ID of the hotel.
   */
  fetchHotelDetails(id: string) {
    this.http.get<any>(`http://127.0.0.1:5000/hotels?hotel_id=${id}`)
      .subscribe(
        data => {
          this.Details = data;
          console.log(this.Details);
        },
        error => {
          console.error('Error fetching hotel details:', error);
        }
      );
  }

  /**
   * Checks if the user is authenticated or shows the login modal.
   * @returns A boolean indicating whether the user is authenticated.
   */
  private checkAuthOrShowLogin(): boolean {
    if (!this.authService.getToken()) {
      this.createMessage('warning', 'Please login first.');
      this.showLoginModal();
      return false;
    }
    return true;
  }

  /**
   * Adds a comment for the hotel.
   * @param id - The ID of the hotel.
   */
  addComment(id: string) {
    if (!this.checkAuthOrShowLogin()) return;
    const headers = new HttpHeaders({
      'Authorization': `Bearer ${this.authService.getToken()}`
    });
    this.http.post<any>(`http://127.0.0.1:5000/reviews/?hotel_id=${id}`, {
      content: this.AddComment.content,
      rating: this.AddComment.rating
    }, { headers })
    .subscribe(
      data => {
        this.createMessage('success', 'Comment added successfully!');
        this.isModalVisible = false;
        this.AddComment = { content: '', rating: null };
        this.fetchComments(id);
      },
      error => {
        this.createMessage('error', 'Failed to add comment.');
      }
    );
  }

  /**
   * Updates a comment for the hotel.
   * @param id - The ID of the comment.
   */
  updateComment(id: string) {
    if (!this.checkAuthOrShowLogin()) return;
    const headers = new HttpHeaders({
      'Authorization': `Bearer ${this.authService.getToken()}`
    });
    this.http.put<any>(`http://127.0.0.1:5000/reviews/${id}`, {
      content: this.AddComment.content,
      rating: this.AddComment.rating
    }, { headers })
    .subscribe(
      data => {
        this.createMessage('success', 'Comment updated successfully!');
        this.isModalVisible = false;
        this.AddComment = { content: '', rating: null };
        this.editingCommentId = null;
        this.fetchComments(this.hotelId!);
      },
      error => {
        this.createMessage('error', 'Failed to update comment.');
      }
    );
  }

  /**
   * Deletes a comment for the hotel.
   * @param commentId - The ID of the comment.
   */
  deleteComment(commentId: string) {
    if (!this.checkAuthOrShowLogin()) return;
    const headers = new HttpHeaders({
      'Authorization': `Bearer ${this.authService.getToken()}`
    });
    this.http.delete<any>(`http://127.0.0.1:5000/reviews/${commentId}`, { headers })
    .subscribe(
      data => {
        this.createMessage('success', 'Comment deleted successfully!');
        this.fetchComments(this.hotelId!);
      },
      error => {
        this.createMessage('error', 'Failed to delete comment.');
      }
    );
  }

  /**
   * Fetches the comments for the hotel from the server.
   * @param id - The ID of the hotel.
   */
  fetchComments(id: string) {
    this.http.get<any>(`http://127.0.0.1:5000/reviews?hotel_id=${id}`)
      .subscribe(
        data => {
          this.Comments = data;
          console.log(this.Comments);
        },
        error => {
          console.error('Error fetching comments:', error);
        }
      );
  }

  /**
   * Shows the modal for adding or editing a comment.
   */
  showModal(): void {
    this.isModalVisible = true;
  }

  /**
   * Shows the login modal.
   */
  showLoginModal(): void {
    this.isLoginModalVisible = true;
  }

  /**
   * Shows the modal for adding a comment.
   */
  showAddCommentModal(): void {
    this.modalTitle = 'Add Comment';
    this.editingCommentId = null;
    this.AddComment = { content: '', rating: null };
    this.isModalVisible = true;
  }

  /**
   * Shows the modal for editing a comment.
   * @param comment - The comment to edit.
   */
  showEditModal(comment: any): void {
    if (!this.checkAuthOrShowLogin()) return;
    this.modalTitle = 'Edit Comment';
    this.editingCommentId = comment._id;
    this.AddComment = { 
      content: comment.content, 
      rating: comment.rating 
    };
    this.isModalVisible = true;
  }

  /**
   * Handles the OK button click in the modal.
   */
  handleOk(): void {
    if (this.editingCommentId) {
      this.updateComment(this.editingCommentId);
    } else if (this.hotelId) {
      this.addComment(this.hotelId);
    }
  }

  /**
   * Handles the OK button click in the login modal.
   */
  handleLoginOk(): void {
    this.authService.login(this.loginForm.username, this.loginForm.password).subscribe(
      response => {
        this.createMessage('success', 'Login successful!');
        this.isLoginModalVisible = false;
        this.loginForm = { username: '', password: '' };
        this.showAddCommentModal();
      },
      error => {
        this.createMessage('error', 'Login failed! Please check your credentials.');
      }
    );
  }

  /**
   * Handles the Cancel button click in the login modal.
   */
  handleLoginCancel(): void {
    this.isLoginModalVisible = false;
    this.loginForm = { username: '', password: '' };
  }

  /**
   * Handles the Cancel button click in the comment modal.
   */
  handleCancel(): void {
    this.isModalVisible = false;
    this.AddComment = { content: '', rating: null };
  }

  /**
   * Creates a message using NzMessageService.
   * @param type - The type of the message.
   * @param content - The content of the message.
   */
  createMessage(type: 'success' | 'error' | 'warning' | 'info', content: string): void {
    this.message.create(type, content);
  }

  /**
   * Checks the login status and shows the add comment modal if logged in.
   */
  checkLoginAndShowModal(): void {
    if (!this.isLoggedIn) {
      this.createMessage('warning', 'Please login first');
      this.showLoginModal();
      return;
    }
    this.showAddCommentModal();
  }
}