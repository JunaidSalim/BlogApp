// src/hooks/useFetchPosts.js
import { useState, useEffect } from "react";
import apiInstance from "../utils/axios";

export const useFetchPosts = () => {
    const [posts, setPosts] = useState([]);
    const [isLoading, setIsLoading] = useState(true);

    const fetchPosts = async () => {
        try {
            const response = await apiInstance.get("posts/list/");
            setPosts(response.data);
        } catch (error) {
            console.error("Failed to fetch posts", error);
        } finally {
            setIsLoading(false);
        }
    };

    useEffect(() => {
        fetchPosts();
    }, []);

    return { posts, isLoading, fetchPosts };
};
