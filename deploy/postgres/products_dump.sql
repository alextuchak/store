--
-- PostgreSQL database dump
--

-- Dumped from database version 16.0 (Debian 16.0-1.pgdg120+1)
-- Dumped by pg_dump version 16.0 (Debian 16.0-1.pgdg120+1)

SET statement_timeout = 0;
SET lock_timeout = 0;
SET idle_in_transaction_session_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SELECT pg_catalog.set_config('search_path', '', false);
SET check_function_bodies = false;
SET xmloption = content;
SET client_min_messages = warning;
SET row_security = off;

--
-- Data for Name: products_products; Type: TABLE DATA; Schema: public; Owner: products_owner
--

INSERT INTO public.products_products (id, name, descriptions, price, quantity, image, category_id, full_descriptions, manufacturer) VALUES (1, 'Nike Air Max 90', 'Мужские кроссовки Nike Air Max 90 черные', 15000.00, 5, 'products_images/p0zkj963ciaahn5gesodswa1mj0o2pkj.jpg', 1, 'Верх:
текстиль натуральная кожа искусственная кожа
Подкладка:
текстиль
Подошва:
резина
Материал:
Верх: текстиль, кожа, иск. кожа, подкладка: текстиль, низ: резина', 'Nike');
INSERT INTO public.products_products (id, name, descriptions, price, quantity, image, category_id, full_descriptions, manufacturer) VALUES (2, 'The North Face Himalayan Down Parka', 'Мужская куртка The North Face Himalayan Down Parka', 25000.00, 2, 'products_images/o0ydbpwvmqkafb7kmbqksunb53jldnku.jpg', 2, 'Прототипом мужскому пуховику The North Face Himalayan Down Parka послужила настоящая альпинистская куртка для покорения горных вершин. Теперь эта легенда высокогорья красуется на городских улицах, не потеряв при этом в функциональности и стиле. Свободная посадка модели позволяет создать многослойный тёплый образ. Верхний слой куртки выполнен из ветрозащитной ткани WindWall™ с пропиткой от влаги.', 'The North Face');
INSERT INTO public.products_products (id, name, descriptions, price, quantity, image, category_id, full_descriptions, manufacturer) VALUES (3, 'STREETBEAT Basic Hoodie', 'Мужская худи STREETBEAT Basic Hoodie неоновый лайм', 5000.00, 3, 'products_images/bfa215ce2616e2b2e3e137c1aa65daec.jpg', 3, 'Классическая мужская худи-кенгуру из новой коллекции Basic от Street Beat выполнена из мягкого и приятного на ощупь футера. Отличную посадку модели обеспечивают эластичные манжеты и резинка на поясе. Базовый силуэт толстовки дополнен сдержанным брендированным принтом и узорчатым шнурком. В переднем кармане удобно греть руки и хранить всякие мелочи', 'STREETBEAT');


--
-- Name: products_products_id_seq; Type: SEQUENCE SET; Schema: public; Owner: products_owner
--

SELECT pg_catalog.setval('public.products_products_id_seq', 3, true);


--
-- PostgreSQL database dump complete
--

