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
import { UpdateuserComponent } from './updateuser/updateuser.component';
import { HomeComponent } from './home/home.component';

const routes:Routes=[
  {path:"",redirectTo:"/home",pathMatch:'full'},
  {path:"adduser",component:AdduserComponent},
  {path:"viewuser",component:ViewuserComponent},
  {path:"home",component:HomeComponent},
  {path:"updateuser/:id",component:UpdateuserComponent}
]

@NgModule({
  declarations: [
    AppComponent,
    NavbarComponent,
    AdduserComponent,
    ViewuserComponent,
    UpdateuserComponent,
    HomeComponent
  ],
  imports: [
    BrowserModule,RouterModule.forRoot(routes),HttpClientModule,ReactiveFormsModule,FormsModule
  ],
  providers: [UserService],
  bootstrap: [AppComponent]
})
export class AppModule { }
