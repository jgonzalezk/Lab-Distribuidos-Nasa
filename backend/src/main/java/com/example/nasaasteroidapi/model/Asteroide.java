package com.example.nasaasteroidapi.model;
import org.springframework.data.mongodb.core.mapping.Document;

import lombok.Data;

import org.bson.codecs.pojo.annotations.BsonId;
import org.bson.types.ObjectId;
import org.springframework.data.annotation.Id;



@Document(value = "asteroids")
@Data
public class Asteroide {
    //@Id
    @BsonId
    private ObjectId _id;
    private Long ID;
    private String Name;
    //private Date Date;
    private Float Absolute_magnitude_h;
    private boolean is_potentially_hazardous_asteroid;
    private Float Estimated_diameter_min;    
    private Float Estimated_diameter_max;    
    private String Relative_velocity_KpS;
    private String orbiting_body;
    private boolean Is_sentry_object;




}
