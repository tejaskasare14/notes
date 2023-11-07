package com.example.services;

import java.util.List;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

import com.example.models.User;
import com.example.repositories.UserRepository;

@Service
public class UserServices {
	
	@Autowired
	UserRepository userRepository;
	
	public List<User> getAllUsers()
	{
		List<User> allUsers=userRepository.findAll();
		return allUsers;
	}
	
	public User createUser(User user)
	{
		
		return userRepository.save(user);
	}

}









