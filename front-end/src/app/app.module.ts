import { BrowserModule } from '@angular/platform-browser';
import { NgModule } from '@angular/core';
import { HttpClientModule } from '@angular/common/http';
import { BrowserAnimationsModule } from '@angular/platform-browser/animations';
import { NzCardModule } from 'ng-zorro-antd/card';
import { NzGridModule } from 'ng-zorro-antd/grid';
import { NzButtonModule } from 'ng-zorro-antd/button';
import { NzIconModule, NZ_ICONS } from 'ng-zorro-antd/icon';
import { NZ_I18N, en_US } from 'ng-zorro-antd/i18n';
import { IconDefinition } from '@ant-design/icons-angular';
import { UserOutline, LockOutline } from '@ant-design/icons-angular/icons';
import { NzBadgeModule } from 'ng-zorro-antd/badge';

/**
 * Array of icons to be used in the application.
 */
const icons: IconDefinition[] = [UserOutline, LockOutline];

/**
 * AppModule is the root module of the application.
 */
@NgModule({
  declarations: [],
  imports: [
    BrowserModule,
    HttpClientModule,
    BrowserAnimationsModule,
    NzCardModule,
    NzGridModule,
    NzButtonModule,
    NzIconModule,
    NzBadgeModule
  ],
  providers: [
    { provide: NZ_I18N, useValue: en_US },
    { provide: NZ_ICONS, useValue: icons }
  ]
})
export class AppModule { }

import { bootstrapApplication } from '@angular/platform-browser';
import { AppComponent } from './app.component';

/**
 * Bootstrap the application with the root component.
 */
bootstrapApplication(AppComponent);