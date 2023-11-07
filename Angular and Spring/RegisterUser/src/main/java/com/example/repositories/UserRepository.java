package com.example.repositories;

import org.springframework.data.jpa.repository.JpaRepository;

import org.springframework.web.bind.annotation.CrossOrigin;

import com.example.models.User;



public interface UserRepository extends JpaRepository<User, Integer>{

}
