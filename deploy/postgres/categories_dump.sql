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
-- Data for Name: products_productcategory; Type: TABLE DATA; Schema: public; Owner: products_owner
--

INSERT INTO public.products_productcategory (id, name, description) VALUES (1, 'Кросовки', 'Кросовки');
INSERT INTO public.products_productcategory (id, name, description) VALUES (2, 'Куртки', 'Куртки');
INSERT INTO public.products_productcategory (id, name, description) VALUES (3, 'Толстовки', 'Толстовки');


--
-- Name: products_productcategory_id_seq; Type: SEQUENCE SET; Schema: public; Owner: products_owner
--

SELECT pg_catalog.setval('public.products_productcategory_id_seq', 3, true);


--
-- PostgreSQL database dump complete
--

