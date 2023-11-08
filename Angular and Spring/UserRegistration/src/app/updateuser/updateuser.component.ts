import { Component, OnInit } from '@angular/core';
import { ActivatedRoute, Router } from '@angular/router';
import { UserService } from '../user.service';
import { User, UserInterface } from '../user';
import { FormBuilder, FormControl, FormGroup } from '@angular/forms';

@Component({
  selector: 'app-updateuser',
  templateUrl: './updateuser.component.html',
  styleUrls: ['./updateuser.component.css']
})
export class UpdateuserComponent implements OnInit{
  constructor(
    private activeRoute:ActivatedRoute,
    private userService:UserService,
    private router:Router,
    private formBuilder:FormBuilder
  ) { }

  id= +this.activeRoute.snapshot.paramMap.get('id')!
  user:User = new User()
  userForm!:FormGroup;
  
  ngOnInit()
  {
    
    this.userForm=this.formBuilder.group({
      name:[''],
      age:[''],
      phone:['']
  })


    //this.userService.getUserById(this.id).subscribe(data => console.log(data))
    this.userService.getUserById(this.id).subscribe(data => this.userForm.patchValue(data))


  }


  submitData()
  {
    

    console.log(this.userForm.value);

    this.user.name = this.userForm.value.name
    this.user.age = this.userForm.value.age
    this.user.phone = this.userForm.value.phone
  
     console.log(this.user);
    

    this.userService.updateUser(this.id,this.user).subscribe(data=>
      {
        console.log(data)
        if(data)
        {
          this.router.navigate(['/viewuser'])
        }
      })

 
   }
}
