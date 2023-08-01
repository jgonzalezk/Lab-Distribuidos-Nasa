package com.example.nasaasteroidapi.controllers;
import org.apache.spark.sql.Column;
import org.springframework.web.bind.annotation.*;

import com.example.nasaasteroidapi.service.AsteroideService;
import lombok.RequiredArgsConstructor;
import static org.apache.spark.sql.functions.*;

import java.util.List;
@CrossOrigin(origins = "*")
@RestController
@RequestMapping("")
@RequiredArgsConstructor
public class AsteroideController {
    private AsteroideService AsteroideService;

    @GetMapping("/total/{fechaInicial}/{fechaFinal}")
    @ResponseBody
    public String total_asteroide(@PathVariable("fechaInicial") String fechaInicial, @PathVariable("fechaFinal") String fechaFinal) {

        try{

            Column fecha0 = to_date(lit(fechaInicial), "yyyy-MM-dd");
            Column fecha1 = to_date(lit(fechaFinal), "yyyy-MM-dd");
            List<String> json = AsteroideService.total_asteroide(fecha0,fecha1).toJSON().collectAsList();
            return "[" + String.join(",", json) + "]";
            

        }catch (Exception e){
            return null;
        }
        
    }


    @GetMapping("/total_historico")
    @ResponseBody
    public Long total_historico(){
        return AsteroideService.total_historico();
    }

    @GetMapping("/total_num/{fechaInicial}/{fechaFinal}")
    @ResponseBody
    public Long total_asteroide_num(@PathVariable("fechaInicial") String fechaInicial, @PathVariable("fechaFinal") String fechaFinal){
        try{

            Column fecha0 = to_date(lit(fechaInicial), "yyyy-MM-dd");
            Column fecha1 = to_date(lit(fechaFinal), "yyyy-MM-dd");
            return AsteroideService.total_asteroide_num(fecha0,fecha1);

        }catch (Exception e){
            return (long) -1;
        }
        
        

    }

    @GetMapping("/total_peligroso/{fechaInicial}/{fechaFinal}")
    @ResponseBody
    public Long total_peligroso(@PathVariable("fechaInicial") String fechaInicial, @PathVariable("fechaFinal") String fechaFinal){
        try{

            // Utiliza la función to_date para convertir la columna a DateType
            Column fecha0 = to_date(lit(fechaInicial), "yyyy-MM-dd");
            Column fecha1 = to_date(lit(fechaFinal), "yyyy-MM-dd");
            return AsteroideService.total_peligroso(fecha0,fecha1);

        }catch (Exception e){
            return (long) -1;
        }

    }

    @GetMapping("/velocidad/{fechaInicial}/{fechaFinal}")
    @ResponseBody
    public Double velocidad_promedio(@PathVariable("fechaInicial") String fechaInicial, @PathVariable("fechaFinal") String fechaFinal){
        //String fechaInicial = "2015-09-08";
        //String fechaFinal = "2015-09-08";
        try{

            // Utiliza la función to_date para convertir la columna a DateType
            Column fecha0 = to_date(lit(fechaInicial), "yyyy-MM-dd");
            Column fecha1 = to_date(lit(fechaFinal), "yyyy-MM-dd");
            return AsteroideService.velocidad_promedio(fecha0,fecha1);

        }catch (Exception e){
            return (double) -1;
        }

    }

    @GetMapping("/velocidad_peligroso/{fechaInicial}/{fechaFinal}")
    @ResponseBody
    public Double velocidad_promedio_peligroso(@PathVariable("fechaInicial") String fechaInicial, @PathVariable("fechaFinal") String fechaFinal){
        try{

            // Utiliza la función to_date para convertir la columna a DateType
            Column fecha0 = to_date(lit(fechaInicial), "yyyy-MM-dd");
            Column fecha1 = to_date(lit(fechaFinal), "yyyy-MM-dd");
            return AsteroideService.velocidad_promedio_peligroso(fecha0,fecha1);

        }catch (Exception e){
            return (double) -1;
        }

    }

    @GetMapping("/tamano/{fechaInicial}/{fechaFinal}")
    @ResponseBody
    public Double tamano_promedio(@PathVariable("fechaInicial") String fechaInicial, @PathVariable("fechaFinal") String fechaFinal){
        try{

            // Utiliza la función to_date para convertir la columna a DateType
            Column fecha0 = to_date(lit(fechaInicial), "yyyy-MM-dd");
            Column fecha1 = to_date(lit(fechaFinal), "yyyy-MM-dd");
            return AsteroideService.tamano_promedio(fecha0,fecha1);

        }catch (Exception e){
            return (double) -1;
        }

    }

    
    @GetMapping("/tamano_peligroso/{fechaInicial}/{fechaFinal}")
    @ResponseBody
    public Double tamano_promedio_peligroso(@PathVariable("fechaInicial") String fechaInicial, @PathVariable("fechaFinal") String fechaFinal){
        try{

            // Utiliza la función to_date para convertir la columna a DateType
            Column fecha0 = to_date(lit(fechaInicial), "yyyy-MM-dd");
            Column fecha1 = to_date(lit(fechaFinal), "yyyy-MM-dd");
            return AsteroideService.tamano_promedio_peligroso(fecha0,fecha1);

        }catch (Exception e){
            return (double) -1;
        }

    }

    


}
