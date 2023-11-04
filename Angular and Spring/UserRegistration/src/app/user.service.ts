import { Injectable } from '@angular/core';
import {HttpClient} from '@angular/common/http'
import { User, UserInterface } from './user';
@Injectable({
  providedIn: 'root'
})
export class UserService {

  constructor(
    private httpClient:HttpClient
  ) { }

  getAllUsers()
  {
    return this.httpClient.get<UserInterface>("http://localhost:8080/users")
  }

  addNewUser(userdata:any)
  {
    this.httpClient.post("http://localhost:8080/users",userdata);
  }
}
