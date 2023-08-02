package com.example.nasaasteroidapi;

import org.apache.spark.api.java.JavaSparkContext;
import org.apache.spark.sql.SparkSession;
import org.springframework.context.annotation.Bean;
import org.springframework.context.annotation.Configuration;

@Configuration
public class SparkConfig {
    @Bean
    public SparkSession sparkSession() {
        return SparkSession.builder()
            //  String mongoURI = "mongodb://" + mongoUsername + ":" + mongoPassword + "@localhost:27017/NASA_data.asteroids";
                .master("local")
                .appName("MongoDBSparkApi")
                .config("spark.mongodb.read.connection.uri", "mongodb://MONGO_USERNAME:MONGO_PASSWORD@host.docker.internal:27017/NASA_data.asteroids")
                .config("spark.mongodb.write.connection.uri", "mongodb://MONGO_USERNAME:MONGO_PASSWORD@host.docker.internal:27017/NASA_data.asteroids")
                //.config("spark.mongodb.read.connection.uri", "mongodb://localhost:27017/NASA_data.asteroids")
                //.config("spark.mongodb.write.connection.uri", "mongodb://localhost:27017/NASA_data.asteroids")
                .getOrCreate();

    }

    @Bean
    public JavaSparkContext javaSparkContext() {
        return new JavaSparkContext(sparkSession().sparkContext());
    }


}
