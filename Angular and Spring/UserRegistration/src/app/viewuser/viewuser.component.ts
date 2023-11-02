import { Component, OnInit } from '@angular/core';
import { UserService } from '../user.service';

@Component({
  selector: 'app-viewuser',
  templateUrl: './viewuser.component.html',
  styleUrls: ['./viewuser.component.css']
})
export class ViewuserComponent implements OnInit{
constructor(private userService:UserService){}

users:any
  ngOnInit(): void {
    this.userService.getAllUsers().subscribe(value => console.log(value._embedded.users))
    this.userService.getAllUsers().subscribe(value => this.users=value._embedded.users)

  }

}
