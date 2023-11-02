package com.example.repositories;

import org.springframework.data.jpa.repository.JpaRepository;
import org.springframework.data.rest.core.annotation.RepositoryRestResource;
import org.springframework.web.bind.annotation.CrossOrigin;

import com.example.models.User;


@CrossOrigin(origins = "http://localhost:4200/")
public interface UserRepository extends JpaRepository<User, Integer>{

}
