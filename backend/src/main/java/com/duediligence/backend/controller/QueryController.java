package com.duediligence.backend.controller;

import com.duediligence.backend.service.PythonService;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.*;

import java.util.Map;

@RestController
@RequestMapping("/api")
@CrossOrigin
public class QueryController {

    private final PythonService pythonService;

    public QueryController(PythonService pythonService) {
        this.pythonService = pythonService;
    }

    @PostMapping("/ask")
    public ResponseEntity<?> ask(@RequestBody Map<String, String> body) {

        String question = body.get("question");

        String response = pythonService.query(question);

        return ResponseEntity.ok(response);
    }

}
