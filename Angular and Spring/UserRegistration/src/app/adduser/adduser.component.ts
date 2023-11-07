import { Component } from '@angular/core';
import { FormGroup,FormControl } from '@angular/forms';
import { UserService } from '../user.service';
import { User } from '../user';
import { Router } from '@angular/router';



@Component({
  selector: 'app-adduser',
  templateUrl: './adduser.component.html',
  styleUrls: ['./adduser.component.css']
})
export class AdduserComponent {

  user:User = new User()
  constructor(private userService:UserService, private router:Router){}

  userForm = new FormGroup({
    name : new FormControl(),
    age:new FormControl(),
    phone:new FormControl()
  })

 
  submitData()
  {
    

    console.log(this.userForm.value);

    this.user.name = this.userForm.value.name
    this.user.age = this.userForm.value.age
    this.user.phone = this.userForm.value.phone
  
    console.log(this.user);
    

    this.userService.addNewUser(this.user).subscribe(data=>console.log(data)
    )

  this.router.navigate(['/viewuser'])
  }
  

}
