import { Component, OnInit } from '@angular/core';
import { FormGroup,FormControl, Validators, FormBuilder } from '@angular/forms';
import { UserService } from '../user.service';
import { User } from '../user';
import { Router } from '@angular/router';



@Component({
  selector: 'app-adduser',
  templateUrl: './adduser.component.html',
  styleUrls: ['./adduser.component.css']
})
export class AdduserComponent implements OnInit{

  user:User = new User()
  userForm!:FormGroup;
  constructor(private userService:UserService, private router:Router, private formBuilder:FormBuilder){}
  ngOnInit(): void 
  {
    this.userForm=this.formBuilder.group({
      name:['',[Validators.minLength(3),Validators.maxLength(10),Validators.required]],
      age:['',[Validators.min(18),Validators.max(30),Validators.required]],
      phone:['']
    })
  }

  get name():FormGroup
  {
    return this.userForm.get("name") as FormGroup
  }

  get age():FormGroup
  {
    return this.userForm.get("age") as FormGroup
  }

 
  submitData()
  {
    

    console.log(this.userForm.value);

    
    

    this.user.name = this.userForm.value.name
    this.user.age = this.userForm.value.age
    this.user.phone = this.userForm.value.phone
  
    console.log(this.user);
    

    this.userService.addNewUser(this.user).subscribe(data=>
      {
        console.log(data)
        if(data)
        {
          this.router.navigate(['/viewuser'])
        }
      })

 
  }
  

}
