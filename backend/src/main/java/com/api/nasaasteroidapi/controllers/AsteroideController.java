package com.api.nasaasteroidapi.controllers;
import java.util.List;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.ResponseBody;
import org.springframework.web.bind.annotation.RestController;
import com.api.nasaasteroidapi.model.Asteroide;
import com.api.nasaasteroidapi.service.AsteroideService;

import lombok.RequiredArgsConstructor;

@RestController
@RequestMapping("/api/v1")
@RequiredArgsConstructor
public class AsteroideController {
    private final AsteroideService AsteroideService;

    @GetMapping
    @ResponseBody
    public List <Asteroide> getAll(){
        return AsteroideService.getAll();

    }
}
