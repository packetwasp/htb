--
-- PostgreSQL database dump
--

-- Dumped from database version 11.7 (Debian 11.7-0+deb10u1)
-- Dumped by pg_dump version 11.7 (Debian 11.7-0+deb10u1)

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

SET default_tablespace = '';

SET default_with_oids = false;

--
-- Name: ar_internal_metadata; Type: TABLE; Schema: public; Owner: rails_dev
--

CREATE TABLE public.ar_internal_metadata (
    key character varying NOT NULL,
    value character varying,
    created_at timestamp(6) without time zone NOT NULL,
    updated_at timestamp(6) without time zone NOT NULL
);


ALTER TABLE public.ar_internal_metadata OWNER TO rails_dev;

--
-- Name: articles; Type: TABLE; Schema: public; Owner: rails_dev
--

CREATE TABLE public.articles (
    id bigint NOT NULL,
    title character varying,
    text text,
    created_at timestamp(6) without time zone NOT NULL,
    updated_at timestamp(6) without time zone NOT NULL,
    user_id integer
);


ALTER TABLE public.articles OWNER TO rails_dev;

--
-- Name: articles_id_seq; Type: SEQUENCE; Schema: public; Owner: rails_dev
--

CREATE SEQUENCE public.articles_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.articles_id_seq OWNER TO rails_dev;

--
-- Name: articles_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: rails_dev
--

ALTER SEQUENCE public.articles_id_seq OWNED BY public.articles.id;


--
-- Name: schema_migrations; Type: TABLE; Schema: public; Owner: rails_dev
--

CREATE TABLE public.schema_migrations (
    version character varying NOT NULL
);


ALTER TABLE public.schema_migrations OWNER TO rails_dev;

--
-- Name: users; Type: TABLE; Schema: public; Owner: rails_dev
--

CREATE TABLE public.users (
    id bigint NOT NULL,
    username character varying,
    email character varying,
    created_at timestamp(6) without time zone NOT NULL,
    updated_at timestamp(6) without time zone NOT NULL,
    password_digest character varying
);


ALTER TABLE public.users OWNER TO rails_dev;

--
-- Name: users_id_seq; Type: SEQUENCE; Schema: public; Owner: rails_dev
--

CREATE SEQUENCE public.users_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.users_id_seq OWNER TO rails_dev;

--
-- Name: users_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: rails_dev
--

ALTER SEQUENCE public.users_id_seq OWNED BY public.users.id;


--
-- Name: articles id; Type: DEFAULT; Schema: public; Owner: rails_dev
--

ALTER TABLE ONLY public.articles ALTER COLUMN id SET DEFAULT nextval('public.articles_id_seq'::regclass);


--
-- Name: users id; Type: DEFAULT; Schema: public; Owner: rails_dev
--

ALTER TABLE ONLY public.users ALTER COLUMN id SET DEFAULT nextval('public.users_id_seq'::regclass);


--
-- Data for Name: ar_internal_metadata; Type: TABLE DATA; Schema: public; Owner: rails_dev
--

COPY public.ar_internal_metadata (key, value, created_at, updated_at) FROM stdin;
environment	development	2020-08-24 08:41:37.144359	2020-08-24 08:41:37.144359
\.


--
-- Data for Name: articles; Type: TABLE DATA; Schema: public; Owner: rails_dev
--

COPY public.articles (id, title, text, created_at, updated_at, user_id) FROM stdin;
7	testtttttttttttt	test	2020-08-25 06:17:38.670018	2020-08-25 06:17:38.670018	\N
6	test333333	test2a34444444444444444444	2020-08-25 06:10:50.161161	2020-08-25 07:04:41.873477	\N
\.


--
-- Data for Name: schema_migrations; Type: TABLE DATA; Schema: public; Owner: rails_dev
--

COPY public.schema_migrations (version) FROM stdin;
20200824090649
20200824092735
20200825071346
20200825072021
20200825073838
\.


--
-- Data for Name: users; Type: TABLE DATA; Schema: public; Owner: rails_dev
--

COPY public.users (id, username, email, created_at, updated_at, password_digest) FROM stdin;
1	bill	bill@mail.htb	2020-08-25 08:13:58.662464	2020-08-25 08:13:58.662464	$2a$12$uhUssB8.HFpT4XpbhclQU.Oizufehl9qqKtmdxTXetojn2FcNncJW
2	jennifer	jennifer@mail.htb	2020-08-25 08:54:42.8483	2020-08-25 08:54:42.8483	$2a$12$ik.0o.TGRwMgUmyOR.Djzuyb/hjisgk2vws1xYC/hxw8M1nFk0MQy
\.


--
-- Name: articles_id_seq; Type: SEQUENCE SET; Schema: public; Owner: rails_dev
--

SELECT pg_catalog.setval('public.articles_id_seq', 10, true);


--
-- Name: users_id_seq; Type: SEQUENCE SET; Schema: public; Owner: rails_dev
--

SELECT pg_catalog.setval('public.users_id_seq', 2, true);


--
-- Name: ar_internal_metadata ar_internal_metadata_pkey; Type: CONSTRAINT; Schema: public; Owner: rails_dev
--

ALTER TABLE ONLY public.ar_internal_metadata
    ADD CONSTRAINT ar_internal_metadata_pkey PRIMARY KEY (key);


--
-- Name: articles articles_pkey; Type: CONSTRAINT; Schema: public; Owner: rails_dev
--

ALTER TABLE ONLY public.articles
    ADD CONSTRAINT articles_pkey PRIMARY KEY (id);


--
-- Name: schema_migrations schema_migrations_pkey; Type: CONSTRAINT; Schema: public; Owner: rails_dev
--

ALTER TABLE ONLY public.schema_migrations
    ADD CONSTRAINT schema_migrations_pkey PRIMARY KEY (version);


--
-- Name: users users_pkey; Type: CONSTRAINT; Schema: public; Owner: rails_dev
--

ALTER TABLE ONLY public.users
    ADD CONSTRAINT users_pkey PRIMARY KEY (id);


--
-- PostgreSQL database dump complete
--

