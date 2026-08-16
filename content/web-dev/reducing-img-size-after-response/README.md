---
title: External Image Optimisation
date:  3 march 2025
layout: post
excerpt: Mehtods to optimise an image after it is imported from an external image source/cdn
permalink: optimise-img-external
---

## Optimising image imported from external source

In order to optimise image there are various methods:
1. Reduce image size (while importing with external source permits)
2. Reduce image quality (while importing with external source permits)
3. Import as webp if external source permits


Some methods I've used so far:
1. When nothing could be done while importing, this method has been applied

    It involves editing the image, drawing it in a canvas and display the redrawn image.

    **code:**
    ```js
    import React, { useState, useEffect } from "react";

    const ImageTransformer = ({ src, maxWidth = 500, quality = 0.7 }) => {
    const [compressedSrc, setCompressedSrc] = useState(null);

    useEffect(() => {
        const compressImage = async () => {
        const img = new Image();
        img.crossOrigin = "anonymous"; // Prevent CORS issues
        img.src = src;

        img.onload = () => {
            const canvas = document.createElement("canvas");
            const ctx = canvas.getContext("2d");

            // Resize while keeping aspect ratio
            const scale = maxWidth / img.width;
            canvas.width = maxWidth;
            canvas.height = img.height * scale;

            // Draw image on the canvas
            ctx.drawImage(img, 0, 0, canvas.width, canvas.height);

            // Convert to compressed WebP format
            const compressedDataUrl = canvas.toDataURL("image/webp", quality);
            setCompressedSrc(compressedDataUrl);
        };
        };

        compressImage();
    }, [src, maxWidth, quality]);

    return (
        <img src={compressedSrc || src} alt="Compressed" width="100%" />
    );
    };

    export default ImageTransformer;

    ```
