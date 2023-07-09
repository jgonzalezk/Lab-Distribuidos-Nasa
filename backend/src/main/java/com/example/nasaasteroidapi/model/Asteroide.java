package com.example.nasaasteroidapi.model;
import org.springframework.data.mongodb.core.mapping.Document;
import java.sql.Date;
import lombok.Data;

import org.bson.codecs.pojo.annotations.BsonId;
import org.bson.types.ObjectId;



@Document(value = "asteroids")
@Data
public class Asteroide {
    @BsonId
    private ObjectId _id;
    private Long ID;
    private String Name;
    private Date Date;
    private Double Absolute_magnitude_h;
    private boolean is_potentially_hazardous_asteroid;
    private Double Estimated_diameter_min;    
    private Double Estimated_diameter_max;    
    private String Relative_velocity_KpS;
    private String orbiting_body;
    private boolean Is_sentry_object;




}
