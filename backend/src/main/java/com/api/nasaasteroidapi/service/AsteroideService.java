package com.api.nasaasteroidapi.service;
import java.util.List;

import org.springframework.stereotype.Service;

import com.api.nasaasteroidapi.model.Asteroide;
import com.api.nasaasteroidapi.repository.AsteroideRepository;

import lombok.RequiredArgsConstructor;


@Service
@RequiredArgsConstructor
public class AsteroideService {
    private final AsteroideRepository AsteroideRepository;

    public List<Asteroide> getAll(){
        return AsteroideRepository.findAll();

    }

}
