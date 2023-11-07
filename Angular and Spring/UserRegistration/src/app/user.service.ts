import { Injectable } from '@angular/core';
import {HttpClient} from '@angular/common/http'
import { User, UserInterface } from './user';
import { Observable } from 'rxjs';
@Injectable({
  providedIn: 'root'
})
export class UserService {

  constructor(
    private httpClient:HttpClient
  ) { }

  getAllUsers()
  {
    return this.httpClient.get<UserInterface[]>("http://localhost:8080/v1/api/users")
  }

  getUserById(id:number)
  {
    return this.httpClient.get<UserInterface>(`http://localhost:8080/v1/api/users/${id}`)
  }

  addNewUser(user :User)
  {
    console.log(user);
    const headers = {'Content-Type':'application/json'}  
    // const body=JSON.stringify(user);
    return this.httpClient.post("http://localhost:8080/v1/api/users",user,{'headers':headers});
  }

  deleteUser(id:number)
  {
      return this.httpClient.delete(`http://localhost:8080/v1/api/users/${id}`)
  }

  updateUser(id:number, user:User)
  {
    const headers = {'Content-Type':'application/json'}  
    return this.httpClient.put(`http://localhost:8080/v1/api/users/${id}`,user,{'headers':headers})
  }

  
}
