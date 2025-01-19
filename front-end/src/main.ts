import { bootstrapApplication } from '@angular/platform-browser';
import { appConfig } from './app/app.config';
import { AppComponent } from './app/app.component';
import { provideHttpClient } from '@angular/common/http';

// Remove the provideRouter from the bootstrap code
// import { provideRouter } from '@angular/router';
// import { routes } from './app/app.routes';

/**
 * Bootstrap the application with the root component and additional providers.
 */
bootstrapApplication(AppComponent, {
  providers: [
    provideHttpClient(),
    // Remove duplicated provideRouter
    // provideRouter(routes),
    ...appConfig.providers
  ]
})
  .catch((err) => console.error(err));