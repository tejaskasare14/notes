import { Component } from '@angular/core';
import { FormGroup,FormControl } from '@angular/forms';
import { UserService } from '../user.service';
import { User } from '../user';


@Component({
  selector: 'app-adduser',
  templateUrl: './adduser.component.html',
  styleUrls: ['./adduser.component.css']
})
export class AdduserComponent {
  constructor(private userService:UserService){}

  userForm = new FormGroup({
    name : new FormControl(),
    age:new FormControl(),
    phone:new FormControl()
  })

 
  submitData()
  {
    

    // console.log(this.userForm.value);
    this.userService.addNewUser(this.userForm.value)

  
  }
  

}
