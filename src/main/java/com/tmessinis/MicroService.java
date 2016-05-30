package com.tmessinis;

import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;

@SpringBootApplication
@RestController
public class MicroService {

    @RequestMapping("/")
    public String home() {
        return "Hello Continuous Delivery World";
    }

    public static void main(String[] args) {
        SpringApplication.run(MicroService.class, args);
    }

}
