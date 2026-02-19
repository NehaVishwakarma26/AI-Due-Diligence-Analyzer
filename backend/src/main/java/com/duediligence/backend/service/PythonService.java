package com.duediligence.backend.service;

import org.springframework.beans.factory.annotation.Value;
import org.springframework.stereotype.Service;
import org.springframework.web.client.RestTemplate;

import java.util.Map;

@Service
public class PythonService {

    @Value("${python.service.url}")
    private String pythonServiceUrl;

    private final RestTemplate restTemplate = new RestTemplate();

    public String ingestDocument(String text, Map<String, Object> metadata) {

        Map<String, Object> body = Map.of(
                "text", text,
                "metadata", metadata
        );

        return restTemplate.postForObject(
                pythonServiceUrl + "/ingest",
                body,
                String.class
        );
    }

    public String query(String question) {

        Map<String, String> body = Map.of(
                "question", question
        );

        return restTemplate.postForObject(
                pythonServiceUrl + "/query",
                body,
                String.class
        );
    }

}
