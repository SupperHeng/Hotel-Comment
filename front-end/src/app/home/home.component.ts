import { Component, OnInit } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { CommonModule } from '@angular/common';
import { FormsModule } from '@angular/forms';
import { NzCardModule } from 'ng-zorro-antd/card';
import { NzGridModule } from 'ng-zorro-antd/grid';
import { NzButtonModule } from 'ng-zorro-antd/button';
import { NzCarouselModule } from 'ng-zorro-antd/carousel';
import { NzImageModule } from 'ng-zorro-antd/image';
import { NzIconModule } from 'ng-zorro-antd/icon';
import { NzRateModule } from 'ng-zorro-antd/rate';
import { NzBadgeModule } from 'ng-zorro-antd/badge';
import { RouterModule, Router } from '@angular/router';

/**
 * HomeComponent is the component for displaying the home page with a list of hotels.
 */
@Component({
  selector: 'app-home',
  templateUrl: './home.component.html',
  styleUrls: ['./home.component.css'],
  standalone: true,
  imports: [
    CommonModule,
    FormsModule,
    NzCardModule,
    NzGridModule,
    NzButtonModule,
    NzCarouselModule,
    NzImageModule,
    NzIconModule,
    NzRateModule,
    NzBadgeModule,
    RouterModule
  ]
})
export class HomeComponent implements OnInit {
  hotels: any[] = [];
  carouselEffect = 'scrollx';

  /**
   * Constructor to initialize the HomeComponent.
   * @param http - HttpClient to make HTTP requests.
   * @param router - Router to navigate to different routes.
   */
  constructor(private http: HttpClient, private router: Router) {}

  /**
   * Lifecycle hook that is called after data-bound properties of a directive are initialized.
   */
  ngOnInit() {
    this.getHotels();
  }

  /**
   * Fetches the list of hotels from the server.
   */
  getHotels() {
    this.http.get<any[]>('http://127.0.0.1:5000/hotels')
      .subscribe(
        data => {
          this.hotels = data;
          console.log(this.hotels);
        },
        error => {
          console.error('Error fetching hotels:', error);
        }
      );
  }

  /**
   * Converts the rating from a 10-point scale to a 5-point scale.
   * @param rating - The rating to convert.
   * @returns The converted rating.
   */
  convertRating(rating: number): number {
    return rating / 2;
  }

  /**
   * Navigates to the details page of a specific hotel.
   * @param id - The ID of the hotel.
   */
  navigateToDetails(id: string) {
    this.router.navigate(['details', id]);
  }
}