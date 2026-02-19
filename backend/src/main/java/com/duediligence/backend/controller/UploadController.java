package com.duediligence.backend.controller;

import com.duediligence.backend.service.PythonService;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.*;
import org.springframework.web.multipart.MultipartFile;

import java.util.Map;

@RestController
@RequestMapping("/api")
@CrossOrigin
public class UploadController {

    private final PythonService pythonService;

    public UploadController(PythonService pythonService) {
        this.pythonService = pythonService;
    }

    @PostMapping("/upload")
    public ResponseEntity<?> upload(
            @RequestParam("file") MultipartFile[] files
    ) throws Exception {

        for (MultipartFile file : files) {
            String content = new String(file.getBytes());

            Map<String, Object> metadata = Map.of(
                    "file_name", file.getOriginalFilename()
            );

            pythonService.ingestDocument(content, metadata);
        }

        return ResponseEntity.ok("Uploaded successfully");
    }


}
