import { Injectable } from '@angular/core';
import {HttpClient} from '@angular/common/http'
import { UserInterface } from './user';
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
}
