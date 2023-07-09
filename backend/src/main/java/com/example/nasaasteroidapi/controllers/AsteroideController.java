package com.example.nasaasteroidapi.controllers;
import org.apache.spark.sql.Column;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.ResponseBody;
import org.springframework.web.bind.annotation.RestController;

import com.example.nasaasteroidapi.model.Asteroide;
import com.example.nasaasteroidapi.service.AsteroideService;

import lombok.RequiredArgsConstructor;
import static org.apache.spark.sql.functions.*;

import java.util.List;
@RestController
@RequestMapping("")
@RequiredArgsConstructor
public class AsteroideController {
    private final AsteroideService AsteroideService;




    @GetMapping("/total")
    @ResponseBody
    public Long total_asteroide(){
        String fechaInicial = "2015-09-08";
        String fechaFinal = "2015-09-08";
        try{

            Column fecha0 = to_date(lit(fechaInicial), "yyyy-MM-dd");
            Column fecha1 = to_date(lit(fechaFinal), "yyyy-MM-dd");
            return AsteroideService.total_asteroide(fecha0,fecha1);

        }catch (Exception e){
            return (long) -1;
        }
        
        

    }

    @GetMapping("/total_peligroso")
    @ResponseBody
    public Long total_peligroso(){
        String fechaInicial = "2015-09-08";
        String fechaFinal = "2015-09-08";
        try{

            // Utiliza la función to_date para convertir la columna a DateType
            Column fecha0 = to_date(lit(fechaInicial), "yyyy-MM-dd");
            Column fecha1 = to_date(lit(fechaFinal), "yyyy-MM-dd");
            return AsteroideService.total_peligroso(fecha0,fecha1);

        }catch (Exception e){
            return (long) -1;
        }

    }

    @GetMapping("/velocidad")
    @ResponseBody
    public Double velocidad_promedio(){
        String fechaInicial = "2015-09-08";
        String fechaFinal = "2015-09-08";
        try{

            // Utiliza la función to_date para convertir la columna a DateType
            Column fecha0 = to_date(lit(fechaInicial), "yyyy-MM-dd");
            Column fecha1 = to_date(lit(fechaFinal), "yyyy-MM-dd");
            return AsteroideService.velocidad_promedio(fecha0,fecha1);

        }catch (Exception e){
            return (double) -1;
        }

    }

    @GetMapping("/velocidad_peligroso")
    @ResponseBody
    public Double velocidad_promedio_peligroso(){
        String fechaInicial = "2015-09-08";
        String fechaFinal = "2015-09-08";
        try{

            // Utiliza la función to_date para convertir la columna a DateType
            Column fecha0 = to_date(lit(fechaInicial), "yyyy-MM-dd");
            Column fecha1 = to_date(lit(fechaFinal), "yyyy-MM-dd");
            return AsteroideService.velocidad_promedio_peligroso(fecha0,fecha1);

        }catch (Exception e){
            return (double) -1;
        }

    }

    @GetMapping("/tamano")
    @ResponseBody
    public Double tamano_promedio(){
        String fechaInicial = "2015-09-08";
        String fechaFinal = "2015-09-08";
        try{

            // Utiliza la función to_date para convertir la columna a DateType
            Column fecha0 = to_date(lit(fechaInicial), "yyyy-MM-dd");
            Column fecha1 = to_date(lit(fechaFinal), "yyyy-MM-dd");
            return AsteroideService.tamano_promedio(fecha0,fecha1);

        }catch (Exception e){
            return (double) -1;
        }

    }

    
    @GetMapping("/tamano_peligroso")
    @ResponseBody
    public Double tamano_promedio_peligroso(){
        String fechaInicial = "2015-09-08";
        String fechaFinal = "2015-09-08";
        try{

            // Utiliza la función to_date para convertir la columna a DateType
            Column fecha0 = to_date(lit(fechaInicial), "yyyy-MM-dd");
            Column fecha1 = to_date(lit(fechaFinal), "yyyy-MM-dd");
            return AsteroideService.tamano_promedio_peligroso(fecha0,fecha1);

        }catch (Exception e){
            return (double) -1;
        }

    }

    public List<Asteroide> getAll() {
        return AsteroideService.getAll();
    }



}
