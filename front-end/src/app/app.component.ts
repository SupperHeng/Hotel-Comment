import { Component } from '@angular/core';
import { RouterModule } from '@angular/router';
import { NzButtonModule } from 'ng-zorro-antd/button';

/**
 * AppComponent is the root component of the application.
 */
@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.css'],
  standalone: true,
  imports: [
    RouterModule,
    NzButtonModule // Import NzButtonModule for using nz-button in the template
  ]
})
export class AppComponent {
  /**
   * Placeholder method for setting the title.
   * @param title - The title to set.
   */
  title(title: any) {
    throw new Error('Method not implemented.');
  }
}