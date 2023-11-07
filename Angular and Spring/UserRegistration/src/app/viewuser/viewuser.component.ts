import { Component, OnInit } from '@angular/core';
import { UserService } from '../user.service';
import { UserInterface } from '../user';

@Component({
  selector: 'app-viewuser',
  templateUrl: './viewuser.component.html',
  styleUrls: ['./viewuser.component.css']
})
export class ViewuserComponent implements OnInit{
constructor(private userService:UserService){}

users!:UserInterface[]
  ngOnInit(): void {
    //this.userService.getAllUsers().subscribe(value => console.log(value))
    this.userService.getAllUsers().subscribe(value => this.users=value)

  }

  deleteUser(id:number)
  {
    this.userService.deleteUser(id).subscribe(value=>
      {
        console.log(value)
        if(value==null)
        {
          window.location.reload();
        }
      })
    
  }
}
