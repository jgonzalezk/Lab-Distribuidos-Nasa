package com.example.nasaasteroidapi.service;

import org.apache.spark.sql.Column;
import org.apache.spark.sql.Dataset;
import org.apache.spark.sql.Row;
import org.apache.spark.sql.SparkSession;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;
import com.example.nasaasteroidapi.repository.AsteroideRepository;

import static org.apache.spark.sql.functions.*;
import lombok.RequiredArgsConstructor;

@Service
@RequiredArgsConstructor
public class AsteroideService {
    @Autowired
    private SparkSession spark;
    private final Dataset<Row> dataframe;

    @Autowired
    public AsteroideService(SparkSession spark) {
        this.spark = spark;
        this.dataframe = spark.read().format("mongodb").load();
        this.dataframe .cache();
    }

    public Long total_historico(){
        Long df = dataframe.count();
        return  df;
    }

    public Dataset<Row> total_asteroide(Column fechaInicial, Column fechaFinal){
        Dataset<Row> df = dataframe
            .where(col("Date").geq(fechaInicial).and(col("Date").leq(to_date(lit(fechaFinal), "yyyy-MM-dd"))));
        return df;
    }



    public Long total_asteroide_num(Column fechaInicial, Column fechaFinal) {
        Long total = dataframe
                .where(col("Date").geq(fechaInicial).and(col("Date").leq(to_date(lit(fechaFinal), "yyyy-MM-dd"))))
                .count();
        return total;

    }

    public Long total_peligroso(Column fechaInicial, Column fechaFinal) {
        Long result = dataframe
                .where("Is_potentially_hazardous_asteroid = true")
                .where(col("Date").geq(fechaInicial).and(col("Date").leq(to_date(lit(fechaFinal), "yyyy-MM-dd"))))
                .count();
        return result;
    }

    public Double velocidad_promedio(Column fechaInicial, Column fechaFinal) {
        Double result = dataframe
                .where(col("Date").geq(fechaInicial).and(col("Date").leq(to_date(lit(fechaFinal), "yyyy-MM-dd"))))
                .agg(avg("Relative_velocity_KpS"))
                .first()
                .getDouble(0);
        return result;

    }

    public Double velocidad_promedio_peligroso(Column fechaInicial, Column fechaFinal) {
        Double result = dataframe
                .where("Is_potentially_hazardous_asteroid = true")
                .where(col("Date").geq(fechaInicial).and(col("Date").leq(to_date(lit(fechaFinal), "yyyy-MM-dd"))))
                .agg(avg("Relative_velocity_KpS"))
                .first()
                .getDouble(0);
        return result;

    }

    public Double tamano_promedio(Column fechaInicial, Column fechaFinal) {
        Double resultMin = dataframe
                .where(col("Date").geq(fechaInicial).and(col("Date").leq(to_date(lit(fechaFinal), "yyyy-MM-dd"))))
                .agg(avg("Estimated_diameter_met_min"))
                .first()
                .getDouble(0);
        Double resultMax = dataframe
                .where(col("Date").geq(fechaInicial).and(col("Date").leq(to_date(lit(fechaFinal), "yyyy-MM-dd"))))
                .agg(avg("Estimated_diameter_met_max"))
                .first()
                .getDouble(0);
        Double result = (resultMax + resultMin) / 2;
        return result;

    }

    public Double tamano_promedio_peligroso(Column fechaInicial, Column fechaFinal) {
        Double resultMin = dataframe
                .where("Is_potentially_hazardous_asteroid = true")
                .where(col("Date").geq(fechaInicial).and(col("Date").leq(to_date(lit(fechaFinal), "yyyy-MM-dd"))))
                .agg(avg("Estimated_diameter_met_min"))
                .first()
                .getDouble(0);
        Double resultMax = dataframe
                .where("Is_potentially_hazardous_asteroid = true")
                .where(col("Date").geq(fechaInicial).and(col("Date").leq(to_date(lit(fechaFinal), "yyyy-MM-dd"))))
                .agg(avg("Estimated_diameter_met_max"))
                .first()
                .getDouble(0);
        Double result = (resultMax + resultMin) / 2;
        return result;

    }

    



}
