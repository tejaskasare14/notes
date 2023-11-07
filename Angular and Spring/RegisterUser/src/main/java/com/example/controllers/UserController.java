package com.example.controllers;

import java.util.List;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.CrossOrigin;
import org.springframework.web.bind.annotation.DeleteMapping;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PathVariable;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.RequestBody;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;

import com.example.models.User;
import com.example.services.UserServices;

@CrossOrigin(origins = "http://localhost:4200/")
@RestController
@RequestMapping("v1/api/users")
public class UserController {
	
	@Autowired
	UserServices userServices;
	
	@GetMapping()
	public List<User> getAllUsers()
	{
		return userServices.getAllUsers();
	}
	
	@PostMapping()
	public User createUser(@RequestBody User user)
	{
		
		return userServices.createUser(user);
	}
	
	
	@DeleteMapping("/{id}")
	public void deleteUser(@PathVariable int id)
	{
		System.out.println(id);
		userServices.deleteUser(id);
	}

}





