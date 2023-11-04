import { NgModule } from '@angular/core';
import { BrowserModule } from '@angular/platform-browser';

import { AppComponent } from './app.component';
import { NavbarComponent } from './navbar/navbar.component';
import { AdduserComponent } from './adduser/adduser.component';
import { ViewuserComponent } from './viewuser/viewuser.component';
import { RouterModule, Routes } from '@angular/router';
import { UserService } from './user.service';
import {HttpClientModule} from '@angular/common/http'
import { ReactiveFormsModule,FormsModule } from '@angular/forms';

const routes:Routes=[
  {path:"adduser",component:AdduserComponent},
  {path:"viewuser",component:ViewuserComponent}
]

@NgModule({
  declarations: [
    AppComponent,
    NavbarComponent,
    AdduserComponent,
    ViewuserComponent
  ],
  imports: [
    BrowserModule,RouterModule.forRoot(routes),HttpClientModule,ReactiveFormsModule,FormsModule
  ],
  providers: [UserService],
  bootstrap: [AppComponent]
})
export class AppModule { }
