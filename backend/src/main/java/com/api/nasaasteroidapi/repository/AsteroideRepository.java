package com.api.nasaasteroidapi.repository;
import com.api.nasaasteroidapi.model.Asteroide;

import org.springframework.data.mongodb.repository.MongoRepository;
import org.springframework.stereotype.Repository;

@Repository
public interface AsteroideRepository extends MongoRepository<Asteroide, String> {

}