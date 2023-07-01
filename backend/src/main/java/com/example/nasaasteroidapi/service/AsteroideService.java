package com.example.nasaasteroidapi.service;
import java.util.List;

import org.apache.spark.SparkConf;
import org.apache.spark.api.java.JavaSparkContext;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;
import org.apache.spark.SparkContext;
import org.apache.spark.SparkConf;
import com.example.nasaasteroidapi.model.Asteroide;
import com.example.nasaasteroidapi.repository.AsteroideRepository;

import lombok.RequiredArgsConstructor;


@Service
@RequiredArgsConstructor
public class AsteroideService {
    private final AsteroideRepository asteroideRepository;
    //private final JavaSparkContext javaSparkContext;
    SparkConf conf = new SparkConf().setAppName("api").setMaster("local");
    JavaSparkContext sc = new JavaSparkContext(conf);

    public List<Asteroide> getAll() {
        return asteroideRepository.findAll();
    }
}

