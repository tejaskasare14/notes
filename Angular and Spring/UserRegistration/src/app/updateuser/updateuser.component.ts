import { Component, OnInit } from '@angular/core';
import { ActivatedRoute, Router } from '@angular/router';
import { UserService } from '../user.service';
import { User, UserInterface } from '../user';
import { FormControl, FormGroup } from '@angular/forms';

@Component({
  selector: 'app-updateuser',
  templateUrl: './updateuser.component.html',
  styleUrls: ['./updateuser.component.css']
})
export class UpdateuserComponent implements OnInit{

  constructor(
    private activeRoute:ActivatedRoute,
    private userService:UserService,
    private router:Router
  ) { }

  user!:UserInterface
  id:number=0

  user_obj:User = new User()

  userForm = new FormGroup({
    name : new FormControl(),
    age:new FormControl(),
    phone:new FormControl()
  })
  ngOnInit(): void {
    this.id= +this.activeRoute.snapshot.paramMap.get('id')!
    console.log(this.id);

    this.userService.getUserById(this.id).subscribe(data => console.log(data))
    this.userService.getUserById(this.id).subscribe(data => this.user=data)
 
  }

  submitData()
  {
    

    console.log(this.userForm.value);

    this.user_obj.name = this.userForm.value.name
    this.user_obj.age = this.userForm.value.age
    this.user_obj.phone = this.userForm.value.phone
  
    console.log(this.user_obj);
    

    this.userService.updateUser(this.id,this.user_obj).subscribe(data=>
      {
        console.log(data)
        if(data)
        {
          this.router.navigate(['/viewuser'])
        }
      })

 
  }
}
