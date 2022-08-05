--
-- PostgreSQL database dump
--

-- Dumped from database version 14.3 (Debian 14.3-1.pgdg110+1)
-- Dumped by pg_dump version 14.3 (Debian 14.3-1.pgdg110+1)

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

SET default_table_access_method = heap;

--
-- Name: auth_group; Type: TABLE; Schema: public; Owner: admin
--

CREATE TABLE public.auth_group (
    id integer NOT NULL,
    name character varying(150) NOT NULL
);


ALTER TABLE public.auth_group OWNER TO admin;

--
-- Name: auth_group_id_seq; Type: SEQUENCE; Schema: public; Owner: admin
--

CREATE SEQUENCE public.auth_group_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.auth_group_id_seq OWNER TO admin;

--
-- Name: auth_group_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: admin
--

ALTER SEQUENCE public.auth_group_id_seq OWNED BY public.auth_group.id;


--
-- Name: auth_group_permissions; Type: TABLE; Schema: public; Owner: admin
--

CREATE TABLE public.auth_group_permissions (
    id bigint NOT NULL,
    group_id integer NOT NULL,
    permission_id integer NOT NULL
);


ALTER TABLE public.auth_group_permissions OWNER TO admin;

--
-- Name: auth_group_permissions_id_seq; Type: SEQUENCE; Schema: public; Owner: admin
--

CREATE SEQUENCE public.auth_group_permissions_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.auth_group_permissions_id_seq OWNER TO admin;

--
-- Name: auth_group_permissions_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: admin
--

ALTER SEQUENCE public.auth_group_permissions_id_seq OWNED BY public.auth_group_permissions.id;


--
-- Name: auth_permission; Type: TABLE; Schema: public; Owner: admin
--

CREATE TABLE public.auth_permission (
    id integer NOT NULL,
    name character varying(255) NOT NULL,
    content_type_id integer NOT NULL,
    codename character varying(100) NOT NULL
);


ALTER TABLE public.auth_permission OWNER TO admin;

--
-- Name: auth_permission_id_seq; Type: SEQUENCE; Schema: public; Owner: admin
--

CREATE SEQUENCE public.auth_permission_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.auth_permission_id_seq OWNER TO admin;

--
-- Name: auth_permission_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: admin
--

ALTER SEQUENCE public.auth_permission_id_seq OWNED BY public.auth_permission.id;


--
-- Name: django_admin_log; Type: TABLE; Schema: public; Owner: admin
--

CREATE TABLE public.django_admin_log (
    id integer NOT NULL,
    action_time timestamp with time zone NOT NULL,
    object_id text,
    object_repr character varying(200) NOT NULL,
    action_flag smallint NOT NULL,
    change_message text NOT NULL,
    content_type_id integer,
    user_id bigint NOT NULL,
    CONSTRAINT django_admin_log_action_flag_check CHECK ((action_flag >= 0))
);


ALTER TABLE public.django_admin_log OWNER TO admin;

--
-- Name: django_admin_log_id_seq; Type: SEQUENCE; Schema: public; Owner: admin
--

CREATE SEQUENCE public.django_admin_log_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.django_admin_log_id_seq OWNER TO admin;

--
-- Name: django_admin_log_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: admin
--

ALTER SEQUENCE public.django_admin_log_id_seq OWNED BY public.django_admin_log.id;


--
-- Name: django_content_type; Type: TABLE; Schema: public; Owner: admin
--

CREATE TABLE public.django_content_type (
    id integer NOT NULL,
    app_label character varying(100) NOT NULL,
    model character varying(100) NOT NULL
);


ALTER TABLE public.django_content_type OWNER TO admin;

--
-- Name: django_content_type_id_seq; Type: SEQUENCE; Schema: public; Owner: admin
--

CREATE SEQUENCE public.django_content_type_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.django_content_type_id_seq OWNER TO admin;

--
-- Name: django_content_type_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: admin
--

ALTER SEQUENCE public.django_content_type_id_seq OWNED BY public.django_content_type.id;


--
-- Name: django_migrations; Type: TABLE; Schema: public; Owner: admin
--

CREATE TABLE public.django_migrations (
    id bigint NOT NULL,
    app character varying(255) NOT NULL,
    name character varying(255) NOT NULL,
    applied timestamp with time zone NOT NULL
);


ALTER TABLE public.django_migrations OWNER TO admin;

--
-- Name: django_migrations_id_seq; Type: SEQUENCE; Schema: public; Owner: admin
--

CREATE SEQUENCE public.django_migrations_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.django_migrations_id_seq OWNER TO admin;

--
-- Name: django_migrations_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: admin
--

ALTER SEQUENCE public.django_migrations_id_seq OWNED BY public.django_migrations.id;


--
-- Name: django_session; Type: TABLE; Schema: public; Owner: admin
--

CREATE TABLE public.django_session (
    session_key character varying(40) NOT NULL,
    session_data text NOT NULL,
    expire_date timestamp with time zone NOT NULL
);


ALTER TABLE public.django_session OWNER TO admin;

--
-- Name: feedback_evaluationfeedback; Type: TABLE; Schema: public; Owner: admin
--

CREATE TABLE public.feedback_evaluationfeedback (
    id bigint NOT NULL,
    rate integer NOT NULL,
    evaluation_metric_id bigint NOT NULL,
    feedback_id bigint NOT NULL
);


ALTER TABLE public.feedback_evaluationfeedback OWNER TO admin;

--
-- Name: feedback_evaluationfeedback_id_seq; Type: SEQUENCE; Schema: public; Owner: admin
--

CREATE SEQUENCE public.feedback_evaluationfeedback_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.feedback_evaluationfeedback_id_seq OWNER TO admin;

--
-- Name: feedback_evaluationfeedback_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: admin
--

ALTER SEQUENCE public.feedback_evaluationfeedback_id_seq OWNED BY public.feedback_evaluationfeedback.id;


--
-- Name: feedback_evaluationmetric; Type: TABLE; Schema: public; Owner: admin
--

CREATE TABLE public.feedback_evaluationmetric (
    id bigint NOT NULL,
    question text NOT NULL,
    hidden boolean NOT NULL
);


ALTER TABLE public.feedback_evaluationmetric OWNER TO admin;

--
-- Name: feedback_evaluationmetric_id_seq; Type: SEQUENCE; Schema: public; Owner: admin
--

CREATE SEQUENCE public.feedback_evaluationmetric_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.feedback_evaluationmetric_id_seq OWNER TO admin;

--
-- Name: feedback_evaluationmetric_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: admin
--

ALTER SEQUENCE public.feedback_evaluationmetric_id_seq OWNED BY public.feedback_evaluationmetric.id;


--
-- Name: feedback_feedback; Type: TABLE; Schema: public; Owner: admin
--

CREATE TABLE public.feedback_feedback (
    id bigint NOT NULL,
    time_of_completion date NOT NULL,
    customer_description text NOT NULL,
    service_request_id bigint NOT NULL
);


ALTER TABLE public.feedback_feedback OWNER TO admin;

--
-- Name: feedback_feedback_id_seq; Type: SEQUENCE; Schema: public; Owner: admin
--

CREATE SEQUENCE public.feedback_feedback_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.feedback_feedback_id_seq OWNER TO admin;

--
-- Name: feedback_feedback_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: admin
--

ALTER SEQUENCE public.feedback_feedback_id_seq OWNED BY public.feedback_feedback.id;


--
-- Name: messaging_message; Type: TABLE; Schema: public; Owner: admin
--

CREATE TABLE public.messaging_message (
    id bigint NOT NULL,
    time_of_creation date NOT NULL,
    customer_id bigint NOT NULL,
    expert_id bigint NOT NULL,
    related_service_request_id bigint NOT NULL
);


ALTER TABLE public.messaging_message OWNER TO admin;

--
-- Name: messaging_message_id_seq; Type: SEQUENCE; Schema: public; Owner: admin
--

CREATE SEQUENCE public.messaging_message_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.messaging_message_id_seq OWNER TO admin;

--
-- Name: messaging_message_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: admin
--

ALTER SEQUENCE public.messaging_message_id_seq OWNED BY public.messaging_message.id;


--
-- Name: messaging_messagecontent; Type: TABLE; Schema: public; Owner: admin
--

CREATE TABLE public.messaging_messagecontent (
    id bigint NOT NULL,
    "time" date NOT NULL,
    text text NOT NULL,
    file character varying(100) NOT NULL,
    parent_message_id bigint NOT NULL,
    sender_id bigint NOT NULL
);


ALTER TABLE public.messaging_messagecontent OWNER TO admin;

--
-- Name: messaging_messagecontent_id_seq; Type: SEQUENCE; Schema: public; Owner: admin
--

CREATE SEQUENCE public.messaging_messagecontent_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.messaging_messagecontent_id_seq OWNER TO admin;

--
-- Name: messaging_messagecontent_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: admin
--

ALTER SEQUENCE public.messaging_messagecontent_id_seq OWNED BY public.messaging_messagecontent.id;


--
-- Name: messaging_ticket; Type: TABLE; Schema: public; Owner: admin
--

CREATE TABLE public.messaging_ticket (
    id bigint NOT NULL,
    topic character varying(30) NOT NULL,
    time_of_creation date NOT NULL,
    status character varying(30) NOT NULL,
    creator_id bigint NOT NULL
);


ALTER TABLE public.messaging_ticket OWNER TO admin;

--
-- Name: messaging_ticket_id_seq; Type: SEQUENCE; Schema: public; Owner: admin
--

CREATE SEQUENCE public.messaging_ticket_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.messaging_ticket_id_seq OWNER TO admin;

--
-- Name: messaging_ticket_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: admin
--

ALTER SEQUENCE public.messaging_ticket_id_seq OWNED BY public.messaging_ticket.id;


--
-- Name: messaging_ticketmessage; Type: TABLE; Schema: public; Owner: admin
--

CREATE TABLE public.messaging_ticketmessage (
    id bigint NOT NULL,
    text text NOT NULL,
    file character varying(100) NOT NULL,
    "time" date NOT NULL,
    sender_id bigint NOT NULL,
    ticket_id bigint NOT NULL
);


ALTER TABLE public.messaging_ticketmessage OWNER TO admin;

--
-- Name: messaging_ticketmessage_id_seq; Type: SEQUENCE; Schema: public; Owner: admin
--

CREATE SEQUENCE public.messaging_ticketmessage_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.messaging_ticketmessage_id_seq OWNER TO admin;

--
-- Name: messaging_ticketmessage_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: admin
--

ALTER SEQUENCE public.messaging_ticketmessage_id_seq OWNED BY public.messaging_ticketmessage.id;


--
-- Name: reporting_reportrequest; Type: TABLE; Schema: public; Owner: admin
--

CREATE TABLE public.reporting_reportrequest (
    id bigint NOT NULL,
    start_time date NOT NULL,
    end_time date NOT NULL,
    report_type character varying(40) NOT NULL,
    report_sort_type character varying(40) NOT NULL,
    request_initiator_id bigint NOT NULL
);


ALTER TABLE public.reporting_reportrequest OWNER TO admin;

--
-- Name: reporting_reportrequest_id_seq; Type: SEQUENCE; Schema: public; Owner: admin
--

CREATE SEQUENCE public.reporting_reportrequest_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.reporting_reportrequest_id_seq OWNER TO admin;

--
-- Name: reporting_reportrequest_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: admin
--

ALTER SEQUENCE public.reporting_reportrequest_id_seq OWNED BY public.reporting_reportrequest.id;


--
-- Name: reporting_reportresponse; Type: TABLE; Schema: public; Owner: admin
--

CREATE TABLE public.reporting_reportresponse (
    id bigint NOT NULL,
    status character varying(30) NOT NULL,
    result_type character varying(30) NOT NULL,
    result bytea NOT NULL,
    request_id bigint NOT NULL
);


ALTER TABLE public.reporting_reportresponse OWNER TO admin;

--
-- Name: reporting_reportresponse_id_seq; Type: SEQUENCE; Schema: public; Owner: admin
--

CREATE SEQUENCE public.reporting_reportresponse_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.reporting_reportresponse_id_seq OWNER TO admin;

--
-- Name: reporting_reportresponse_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: admin
--

ALTER SEQUENCE public.reporting_reportresponse_id_seq OWNED BY public.reporting_reportresponse.id;


--
-- Name: services_requestrejectionrelation; Type: TABLE; Schema: public; Owner: admin
--

CREATE TABLE public.services_requestrejectionrelation (
    id bigint NOT NULL,
    expert_id bigint NOT NULL,
    request_id bigint NOT NULL
);


ALTER TABLE public.services_requestrejectionrelation OWNER TO admin;

--
-- Name: services_requestrejectionrelation_id_seq; Type: SEQUENCE; Schema: public; Owner: admin
--

CREATE SEQUENCE public.services_requestrejectionrelation_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.services_requestrejectionrelation_id_seq OWNER TO admin;

--
-- Name: services_requestrejectionrelation_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: admin
--

ALTER SEQUENCE public.services_requestrejectionrelation_id_seq OWNED BY public.services_requestrejectionrelation.id;


--
-- Name: services_service; Type: TABLE; Schema: public; Owner: admin
--

CREATE TABLE public.services_service (
    id bigint NOT NULL,
    name character varying(20) NOT NULL,
    description text NOT NULL,
    category_id bigint NOT NULL
);


ALTER TABLE public.services_service OWNER TO admin;

--
-- Name: services_service_id_seq; Type: SEQUENCE; Schema: public; Owner: admin
--

CREATE SEQUENCE public.services_service_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.services_service_id_seq OWNER TO admin;

--
-- Name: services_service_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: admin
--

ALTER SEQUENCE public.services_service_id_seq OWNED BY public.services_service.id;


--
-- Name: services_servicecategory; Type: TABLE; Schema: public; Owner: admin
--

CREATE TABLE public.services_servicecategory (
    id bigint NOT NULL,
    name character varying(20) NOT NULL,
    description text NOT NULL,
    parent_id bigint
);


ALTER TABLE public.services_servicecategory OWNER TO admin;

--
-- Name: services_servicecategory_id_seq; Type: SEQUENCE; Schema: public; Owner: admin
--

CREATE SEQUENCE public.services_servicecategory_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.services_servicecategory_id_seq OWNER TO admin;

--
-- Name: services_servicecategory_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: admin
--

ALTER SEQUENCE public.services_servicecategory_id_seq OWNED BY public.services_servicecategory.id;


--
-- Name: services_servicerequest; Type: TABLE; Schema: public; Owner: admin
--

CREATE TABLE public.services_servicerequest (
    id bigint NOT NULL,
    status character varying(30) NOT NULL,
    request_type character varying(30) NOT NULL,
    customer_id bigint NOT NULL,
    expert_id bigint,
    service_id bigint NOT NULL,
    created_at timestamp with time zone
);


ALTER TABLE public.services_servicerequest OWNER TO admin;

--
-- Name: services_servicerequest_id_seq; Type: SEQUENCE; Schema: public; Owner: admin
--

CREATE SEQUENCE public.services_servicerequest_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.services_servicerequest_id_seq OWNER TO admin;

--
-- Name: services_servicerequest_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: admin
--

ALTER SEQUENCE public.services_servicerequest_id_seq OWNED BY public.services_servicerequest.id;


--
-- Name: users_customer; Type: TABLE; Schema: public; Owner: admin
--

CREATE TABLE public.users_customer (
    role_ptr_id bigint NOT NULL,
    address text
);


ALTER TABLE public.users_customer OWNER TO admin;

--
-- Name: users_expert; Type: TABLE; Schema: public; Owner: admin
--

CREATE TABLE public.users_expert (
    role_ptr_id bigint NOT NULL,
    document character varying(100),
    expertise_id bigint NOT NULL,
    status boolean NOT NULL
);


ALTER TABLE public.users_expert OWNER TO admin;

--
-- Name: users_itmanager; Type: TABLE; Schema: public; Owner: admin
--

CREATE TABLE public.users_itmanager (
    role_ptr_id bigint NOT NULL
);


ALTER TABLE public.users_itmanager OWNER TO admin;

--
-- Name: users_manager; Type: TABLE; Schema: public; Owner: admin
--

CREATE TABLE public.users_manager (
    role_ptr_id bigint NOT NULL
);


ALTER TABLE public.users_manager OWNER TO admin;

--
-- Name: users_role; Type: TABLE; Schema: public; Owner: admin
--

CREATE TABLE public.users_role (
    id bigint NOT NULL,
    name character varying(20) NOT NULL,
    polymorphic_ctype_id integer
);


ALTER TABLE public.users_role OWNER TO admin;

--
-- Name: users_role_id_seq; Type: SEQUENCE; Schema: public; Owner: admin
--

CREATE SEQUENCE public.users_role_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.users_role_id_seq OWNER TO admin;

--
-- Name: users_role_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: admin
--

ALTER SEQUENCE public.users_role_id_seq OWNED BY public.users_role.id;


--
-- Name: users_user; Type: TABLE; Schema: public; Owner: admin
--

CREATE TABLE public.users_user (
    id bigint NOT NULL,
    password character varying(128) NOT NULL,
    last_login timestamp with time zone,
    is_superuser boolean NOT NULL,
    first_name character varying(150) NOT NULL,
    last_name character varying(150) NOT NULL,
    is_staff boolean NOT NULL,
    is_active boolean NOT NULL,
    date_joined timestamp with time zone NOT NULL,
    username character varying(50),
    email character varying(254) NOT NULL,
    phone_number character varying(11) NOT NULL,
    name character varying(50) NOT NULL,
    role_id bigint
);


ALTER TABLE public.users_user OWNER TO admin;

--
-- Name: users_user_groups; Type: TABLE; Schema: public; Owner: admin
--

CREATE TABLE public.users_user_groups (
    id bigint NOT NULL,
    user_id bigint NOT NULL,
    group_id integer NOT NULL
);


ALTER TABLE public.users_user_groups OWNER TO admin;

--
-- Name: users_user_groups_id_seq; Type: SEQUENCE; Schema: public; Owner: admin
--

CREATE SEQUENCE public.users_user_groups_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.users_user_groups_id_seq OWNER TO admin;

--
-- Name: users_user_groups_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: admin
--

ALTER SEQUENCE public.users_user_groups_id_seq OWNED BY public.users_user_groups.id;


--
-- Name: users_user_id_seq; Type: SEQUENCE; Schema: public; Owner: admin
--

CREATE SEQUENCE public.users_user_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.users_user_id_seq OWNER TO admin;

--
-- Name: users_user_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: admin
--

ALTER SEQUENCE public.users_user_id_seq OWNED BY public.users_user.id;


--
-- Name: users_user_user_permissions; Type: TABLE; Schema: public; Owner: admin
--

CREATE TABLE public.users_user_user_permissions (
    id bigint NOT NULL,
    user_id bigint NOT NULL,
    permission_id integer NOT NULL
);


ALTER TABLE public.users_user_user_permissions OWNER TO admin;

--
-- Name: users_user_user_permissions_id_seq; Type: SEQUENCE; Schema: public; Owner: admin
--

CREATE SEQUENCE public.users_user_user_permissions_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.users_user_user_permissions_id_seq OWNER TO admin;

--
-- Name: users_user_user_permissions_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: admin
--

ALTER SEQUENCE public.users_user_user_permissions_id_seq OWNED BY public.users_user_user_permissions.id;


--
-- Name: auth_group id; Type: DEFAULT; Schema: public; Owner: admin
--

ALTER TABLE ONLY public.auth_group ALTER COLUMN id SET DEFAULT nextval('public.auth_group_id_seq'::regclass);


--
-- Name: auth_group_permissions id; Type: DEFAULT; Schema: public; Owner: admin
--

ALTER TABLE ONLY public.auth_group_permissions ALTER COLUMN id SET DEFAULT nextval('public.auth_group_permissions_id_seq'::regclass);


--
-- Name: auth_permission id; Type: DEFAULT; Schema: public; Owner: admin
--

ALTER TABLE ONLY public.auth_permission ALTER COLUMN id SET DEFAULT nextval('public.auth_permission_id_seq'::regclass);


--
-- Name: django_admin_log id; Type: DEFAULT; Schema: public; Owner: admin
--

ALTER TABLE ONLY public.django_admin_log ALTER COLUMN id SET DEFAULT nextval('public.django_admin_log_id_seq'::regclass);


--
-- Name: django_content_type id; Type: DEFAULT; Schema: public; Owner: admin
--

ALTER TABLE ONLY public.django_content_type ALTER COLUMN id SET DEFAULT nextval('public.django_content_type_id_seq'::regclass);


--
-- Name: django_migrations id; Type: DEFAULT; Schema: public; Owner: admin
--

ALTER TABLE ONLY public.django_migrations ALTER COLUMN id SET DEFAULT nextval('public.django_migrations_id_seq'::regclass);


--
-- Name: feedback_evaluationfeedback id; Type: DEFAULT; Schema: public; Owner: admin
--

ALTER TABLE ONLY public.feedback_evaluationfeedback ALTER COLUMN id SET DEFAULT nextval('public.feedback_evaluationfeedback_id_seq'::regclass);


--
-- Name: feedback_evaluationmetric id; Type: DEFAULT; Schema: public; Owner: admin
--

ALTER TABLE ONLY public.feedback_evaluationmetric ALTER COLUMN id SET DEFAULT nextval('public.feedback_evaluationmetric_id_seq'::regclass);


--
-- Name: feedback_feedback id; Type: DEFAULT; Schema: public; Owner: admin
--

ALTER TABLE ONLY public.feedback_feedback ALTER COLUMN id SET DEFAULT nextval('public.feedback_feedback_id_seq'::regclass);


--
-- Name: messaging_message id; Type: DEFAULT; Schema: public; Owner: admin
--

ALTER TABLE ONLY public.messaging_message ALTER COLUMN id SET DEFAULT nextval('public.messaging_message_id_seq'::regclass);


--
-- Name: messaging_messagecontent id; Type: DEFAULT; Schema: public; Owner: admin
--

ALTER TABLE ONLY public.messaging_messagecontent ALTER COLUMN id SET DEFAULT nextval('public.messaging_messagecontent_id_seq'::regclass);


--
-- Name: messaging_ticket id; Type: DEFAULT; Schema: public; Owner: admin
--

ALTER TABLE ONLY public.messaging_ticket ALTER COLUMN id SET DEFAULT nextval('public.messaging_ticket_id_seq'::regclass);


--
-- Name: messaging_ticketmessage id; Type: DEFAULT; Schema: public; Owner: admin
--

ALTER TABLE ONLY public.messaging_ticketmessage ALTER COLUMN id SET DEFAULT nextval('public.messaging_ticketmessage_id_seq'::regclass);


--
-- Name: reporting_reportrequest id; Type: DEFAULT; Schema: public; Owner: admin
--

ALTER TABLE ONLY public.reporting_reportrequest ALTER COLUMN id SET DEFAULT nextval('public.reporting_reportrequest_id_seq'::regclass);


--
-- Name: reporting_reportresponse id; Type: DEFAULT; Schema: public; Owner: admin
--

ALTER TABLE ONLY public.reporting_reportresponse ALTER COLUMN id SET DEFAULT nextval('public.reporting_reportresponse_id_seq'::regclass);


--
-- Name: services_requestrejectionrelation id; Type: DEFAULT; Schema: public; Owner: admin
--

ALTER TABLE ONLY public.services_requestrejectionrelation ALTER COLUMN id SET DEFAULT nextval('public.services_requestrejectionrelation_id_seq'::regclass);


--
-- Name: services_service id; Type: DEFAULT; Schema: public; Owner: admin
--

ALTER TABLE ONLY public.services_service ALTER COLUMN id SET DEFAULT nextval('public.services_service_id_seq'::regclass);


--
-- Name: services_servicecategory id; Type: DEFAULT; Schema: public; Owner: admin
--

ALTER TABLE ONLY public.services_servicecategory ALTER COLUMN id SET DEFAULT nextval('public.services_servicecategory_id_seq'::regclass);


--
-- Name: services_servicerequest id; Type: DEFAULT; Schema: public; Owner: admin
--

ALTER TABLE ONLY public.services_servicerequest ALTER COLUMN id SET DEFAULT nextval('public.services_servicerequest_id_seq'::regclass);


--
-- Name: users_role id; Type: DEFAULT; Schema: public; Owner: admin
--

ALTER TABLE ONLY public.users_role ALTER COLUMN id SET DEFAULT nextval('public.users_role_id_seq'::regclass);


--
-- Name: users_user id; Type: DEFAULT; Schema: public; Owner: admin
--

ALTER TABLE ONLY public.users_user ALTER COLUMN id SET DEFAULT nextval('public.users_user_id_seq'::regclass);


--
-- Name: users_user_groups id; Type: DEFAULT; Schema: public; Owner: admin
--

ALTER TABLE ONLY public.users_user_groups ALTER COLUMN id SET DEFAULT nextval('public.users_user_groups_id_seq'::regclass);


--
-- Name: users_user_user_permissions id; Type: DEFAULT; Schema: public; Owner: admin
--

ALTER TABLE ONLY public.users_user_user_permissions ALTER COLUMN id SET DEFAULT nextval('public.users_user_user_permissions_id_seq'::regclass);


--
-- Data for Name: auth_group; Type: TABLE DATA; Schema: public; Owner: admin
--

COPY public.auth_group (id, name) FROM stdin;
\.


--
-- Data for Name: auth_group_permissions; Type: TABLE DATA; Schema: public; Owner: admin
--

COPY public.auth_group_permissions (id, group_id, permission_id) FROM stdin;
\.


--
-- Data for Name: auth_permission; Type: TABLE DATA; Schema: public; Owner: admin
--

COPY public.auth_permission (id, name, content_type_id, codename) FROM stdin;
1	Can add log entry	1	add_logentry
2	Can change log entry	1	change_logentry
3	Can delete log entry	1	delete_logentry
4	Can view log entry	1	view_logentry
5	Can add permission	2	add_permission
6	Can change permission	2	change_permission
7	Can delete permission	2	delete_permission
8	Can view permission	2	view_permission
9	Can add group	3	add_group
10	Can change group	3	change_group
11	Can delete group	3	delete_group
12	Can view group	3	view_group
13	Can add content type	4	add_contenttype
14	Can change content type	4	change_contenttype
15	Can delete content type	4	delete_contenttype
16	Can view content type	4	view_contenttype
17	Can add session	5	add_session
18	Can change session	5	change_session
19	Can delete session	5	delete_session
20	Can view session	5	view_session
21	Can add evaluation feedback	6	add_evaluationfeedback
22	Can change evaluation feedback	6	change_evaluationfeedback
23	Can delete evaluation feedback	6	delete_evaluationfeedback
24	Can view evaluation feedback	6	view_evaluationfeedback
25	Can add evaluation metric	7	add_evaluationmetric
26	Can change evaluation metric	7	change_evaluationmetric
27	Can delete evaluation metric	7	delete_evaluationmetric
28	Can view evaluation metric	7	view_evaluationmetric
29	Can add feedback	8	add_feedback
30	Can change feedback	8	change_feedback
31	Can delete feedback	8	delete_feedback
32	Can view feedback	8	view_feedback
33	Can add role	9	add_role
34	Can change role	9	change_role
35	Can delete role	9	delete_role
36	Can view role	9	view_role
37	Can add Customer	10	add_customer
38	Can change Customer	10	change_customer
39	Can delete Customer	10	delete_customer
40	Can view Customer	10	view_customer
41	Can add ITManager	11	add_itmanager
42	Can change ITManager	11	change_itmanager
43	Can delete ITManager	11	delete_itmanager
44	Can view ITManager	11	view_itmanager
45	Can add Manager	12	add_manager
46	Can change Manager	12	change_manager
47	Can delete Manager	12	delete_manager
48	Can view Manager	12	view_manager
49	Can add user	13	add_user
50	Can change user	13	change_user
51	Can delete user	13	delete_user
52	Can view user	13	view_user
53	Can add Expert	14	add_expert
54	Can change Expert	14	change_expert
55	Can delete Expert	14	delete_expert
56	Can view Expert	14	view_expert
57	Can add service	15	add_service
58	Can change service	15	change_service
59	Can delete service	15	delete_service
60	Can view service	15	view_service
61	Can add ServiceCategory	16	add_servicecategory
62	Can change ServiceCategory	16	change_servicecategory
63	Can delete ServiceCategory	16	delete_servicecategory
64	Can view ServiceCategory	16	view_servicecategory
65	Can add service request	17	add_servicerequest
66	Can change service request	17	change_servicerequest
67	Can delete service request	17	delete_servicerequest
68	Can view service request	17	view_servicerequest
69	Can add message	18	add_message
70	Can change message	18	change_message
71	Can delete message	18	delete_message
72	Can view message	18	view_message
73	Can add message content	19	add_messagecontent
74	Can change message content	19	change_messagecontent
75	Can delete message content	19	delete_messagecontent
76	Can view message content	19	view_messagecontent
77	Can add ticket	20	add_ticket
78	Can change ticket	20	change_ticket
79	Can delete ticket	20	delete_ticket
80	Can view ticket	20	view_ticket
81	Can add ticket message	21	add_ticketmessage
82	Can change ticket message	21	change_ticketmessage
83	Can delete ticket message	21	delete_ticketmessage
84	Can view ticket message	21	view_ticketmessage
85	Can add report request	22	add_reportrequest
86	Can change report request	22	change_reportrequest
87	Can delete report request	22	delete_reportrequest
88	Can view report request	22	view_reportrequest
89	Can add report response	23	add_reportresponse
90	Can change report response	23	change_reportresponse
91	Can delete report response	23	delete_reportresponse
92	Can view report response	23	view_reportresponse
93	Can add request rejection relation	24	add_requestrejectionrelation
94	Can change request rejection relation	24	change_requestrejectionrelation
95	Can delete request rejection relation	24	delete_requestrejectionrelation
96	Can view request rejection relation	24	view_requestrejectionrelation
\.


--
-- Data for Name: django_admin_log; Type: TABLE DATA; Schema: public; Owner: admin
--

COPY public.django_admin_log (id, action_time, object_id, object_repr, action_flag, change_message, content_type_id, user_id) FROM stdin;
1	2022-07-18 19:42:26.917119+00	1	حمل و نقل	1	[{"added": {}}]	16	1
2	2022-07-18 19:42:35.51205+00	2	نظافت	1	[{"added": {}}]	16	1
3	2022-07-18 19:42:46.74498+00	3	فنی	1	[{"added": {}}]	16	1
4	2022-07-18 19:42:58.659505+00	4	آشپزخانه --> فنی	1	[{"added": {}}]	16	1
5	2022-07-18 19:43:14.807232+00	5	تغمیر ظرف‌شویی --> آشپزخانه --> فنی	1	[{"added": {}}]	16	1
6	2022-07-18 19:43:28.524433+00	6	نظافت میز --> نظافت	1	[{"added": {}}]	16	1
7	2022-07-18 19:44:25.941254+00	6	نظافت میز --> نظافت	3		16	1
8	2022-07-18 19:44:25.942878+00	5	تغمیر ظرف‌شویی --> آشپزخانه --> فنی	3		16	1
9	2022-07-18 19:44:41.84317+00	1	نظافت میز --> نظافت	1	[{"added": {}}]	15	1
10	2022-07-18 19:44:56.745574+00	2	تعمیر ظرف‌شویی --> آشپزخانه --> فنی	1	[{"added": {}}]	15	1
11	2022-07-18 20:14:35.055776+00	5	Expert object (5)	2	[{"changed": {"fields": ["Status"]}}]	14	1
12	2022-07-19 16:40:32.87637+00	7	تلویزیون --> فنی	1	[{"added": {}}]	16	1
13	2022-07-19 19:44:56.79592+00	3	تعمیر آنتن --> تلویزیون --> فنی	1	[{"added": {}}]	15	1
14	2022-07-21 08:42:30.977098+00	9	\nrequest: نظافت میز <-- نظافت |\nfrom: customer |\nexpert: expert3 |\nstatus: WAIT_FOR_EXPERT_APPROVAL \t	3		17	1
15	2022-07-21 08:42:30.979435+00	8	\nrequest: نظافت میز <-- نظافت |\nfrom: customer |\nexpert: expert2 |\nstatus: WAIT_FOR_EXPERT_APPROVAL \t	3		17	1
16	2022-07-21 08:42:30.980231+00	7	\nrequest: تعمیر ظرف‌شویی <-- آشپزخانه <-- فنی |\nfrom: customer |\nexpert: expert |\nstatus: WAIT_FOR_EXPERT_APPROVAL \t	3		17	1
17	2022-07-21 08:42:30.980919+00	6	\nrequest: نظافت میز <-- نظافت |\nfrom: customer |\nexpert: expert3 |\nstatus: WAIT_FOR_EXPERT_APPROVAL \t	3		17	1
18	2022-07-21 08:49:01.625631+00	14	\nrequest: تعمیر ظرف‌شویی <-- آشپزخانه <-- فنی |\nfrom: customer |\nexpert: expert |\nstatus: WAIT_FOR_EXPERT_APPROVAL \t	3		17	1
19	2022-07-21 08:49:01.632832+00	13	\nrequest: نظافت میز <-- نظافت |\nfrom: customer |\nexpert: expert3 |\nstatus: WAIT_FOR_EXPERT_APPROVAL \t	3		17	1
20	2022-07-21 08:49:01.6336+00	12	\nrequest: نظافت میز <-- نظافت |\nfrom: customer |\nexpert: expert2 |\nstatus: WAIT_FOR_EXPERT_APPROVAL \t	3		17	1
21	2022-07-21 08:49:01.634255+00	11	\nrequest: نظافت میز <-- نظافت |\nfrom: customer |\nexpert: expert3 |\nstatus: WAIT_FOR_EXPERT_APPROVAL \t	3		17	1
22	2022-07-21 08:49:01.634878+00	10	\nrequest: نظافت میز <-- نظافت |\nfrom: customer |\nexpert: expert2 |\nstatus: WAIT_FOR_EXPERT_APPROVAL \t	3		17	1
23	2022-07-21 08:55:23.340495+00	17	\nrequest: تعمیر ظرف‌شویی <-- آشپزخانه <-- فنی |\nfrom: customer |\nexpert: expert |\nstatus: WAIT_FOR_EXPERT_APPROVAL \t	3		17	1
24	2022-07-21 08:55:23.347896+00	16	\nrequest: تعمیر ظرف‌شویی <-- آشپزخانه <-- فنی |\nfrom: customer |\nexpert: expert |\nstatus: WAIT_FOR_EXPERT_APPROVAL \t	3		17	1
25	2022-07-21 08:55:23.348999+00	15	\nrequest: تعمیر ظرف‌شویی <-- آشپزخانه <-- فنی |\nfrom: customer |\nexpert: expert |\nstatus: WAIT_FOR_EXPERT_APPROVAL \t	3		17	1
26	2022-07-21 09:21:02.704553+00	18	\nrequest: تعمیر ظرف‌شویی <-- آشپزخانه <-- فنی |\nfrom: customer2 |\nexpert: expert4 |\nstatus: WAIT_FOR_EXPERT_APPROVAL \t	3		17	1
27	2022-07-23 16:01:43.823357+00	8	Expert object (8)	2	[{"changed": {"fields": ["Status"]}}]	14	1
28	2022-07-23 16:04:50.623652+00	33	\nrequest: تعمیر آنتن <-- تلویزیون <-- فنی |\nfrom: customer |\nexpert: None |\nstatus: NO_EXPERT_FOUND \t	3		17	1
29	2022-07-23 16:04:50.63121+00	32	\nrequest: تعمیر آنتن <-- تلویزیون <-- فنی |\nfrom: customer |\nexpert: None |\nstatus: NO_EXPERT_FOUND \t	3		17	1
30	2022-07-23 16:04:50.632081+00	31	\nrequest: تعمیر آنتن <-- تلویزیون <-- فنی |\nfrom: customer |\nexpert: None |\nstatus: NO_EXPERT_FOUND \t	3		17	1
31	2022-07-23 16:04:50.632965+00	30	\nrequest: تعمیر ظرف‌شویی <-- آشپزخانه <-- فنی |\nfrom: customer2 |\nexpert: expert4 |\nstatus: FINISHED \t	3		17	1
32	2022-07-23 16:04:50.633741+00	29	\nrequest: نظافت میز <-- نظافت |\nfrom: customer2 |\nexpert: expert2 |\nstatus: FINISHED \t	3		17	1
33	2022-07-23 16:04:50.634394+00	28	\nrequest: نظافت میز <-- نظافت |\nfrom: customer2 |\nexpert: expert2 |\nstatus: CANCELED_BY_EXPERT \t	3		17	1
34	2022-07-23 16:04:50.635017+00	27	\nrequest: تعمیر ظرف‌شویی <-- آشپزخانه <-- فنی |\nfrom: customer2 |\nexpert: expert4 |\nstatus: WAIT_FOR_EXPERT_APPROVAL \t	3		17	1
35	2022-07-23 16:04:50.6356+00	26	\nrequest: تعمیر ظرف‌شویی <-- آشپزخانه <-- فنی |\nfrom: customer2 |\nexpert: expert4 |\nstatus: CANCELED_BY_EXPERT \t	3		17	1
36	2022-07-23 16:04:50.636165+00	25	\nrequest: تعمیر ظرف‌شویی <-- آشپزخانه <-- فنی |\nfrom: customer2 |\nexpert: expert4 |\nstatus: IN_PROGRESS \t	3		17	1
37	2022-07-23 16:04:50.636715+00	24	\nrequest: نظافت میز <-- نظافت |\nfrom: customer2 |\nexpert: expert2 |\nstatus: EXPERT_FOUND \t	3		17	1
38	2022-07-23 16:04:50.637307+00	23	\nrequest: نظافت میز <-- نظافت |\nfrom: customer2 |\nexpert: expert3 |\nstatus: IN_PROGRESS \t	3		17	1
39	2022-07-23 16:04:50.637888+00	22	\nrequest: تعمیر ظرف‌شویی <-- آشپزخانه <-- فنی |\nfrom: customer2 |\nexpert: expert4 |\nstatus: IN_PROGRESS \t	3		17	1
40	2022-07-23 16:04:50.638469+00	21	\nrequest: نظافت میز <-- نظافت |\nfrom: customer2 |\nexpert: expert3 |\nstatus: NO_EXPERT_FOUND \t	3		17	1
41	2022-07-23 16:04:50.639015+00	20	\nrequest: نظافت میز <-- نظافت |\nfrom: customer2 |\nexpert: expert2 |\nstatus: EXPERT_FOUND \t	3		17	1
42	2022-07-23 16:04:50.639548+00	19	\nrequest: تعمیر ظرف‌شویی <-- آشپزخانه <-- فنی |\nfrom: customer2 |\nexpert: expert4 |\nstatus: FINISHED \t	3		17	1
\.


--
-- Data for Name: django_content_type; Type: TABLE DATA; Schema: public; Owner: admin
--

COPY public.django_content_type (id, app_label, model) FROM stdin;
1	admin	logentry
2	auth	permission
3	auth	group
4	contenttypes	contenttype
5	sessions	session
6	feedback	evaluationfeedback
7	feedback	evaluationmetric
8	feedback	feedback
9	users	role
10	users	customer
11	users	itmanager
12	users	manager
13	users	user
14	users	expert
15	services	service
16	services	servicecategory
17	services	servicerequest
18	messaging	message
19	messaging	messagecontent
20	messaging	ticket
21	messaging	ticketmessage
22	reporting	reportrequest
23	reporting	reportresponse
24	services	requestrejectionrelation
\.


--
-- Data for Name: django_migrations; Type: TABLE DATA; Schema: public; Owner: admin
--

COPY public.django_migrations (id, app, name, applied) FROM stdin;
1	services	0001_initial	2022-07-18 19:14:23.363583+00
2	contenttypes	0001_initial	2022-07-18 19:14:23.370856+00
3	contenttypes	0002_remove_content_type_name	2022-07-18 19:14:23.376098+00
4	auth	0001_initial	2022-07-18 19:14:23.399344+00
5	auth	0002_alter_permission_name_max_length	2022-07-18 19:14:23.409205+00
6	auth	0003_alter_user_email_max_length	2022-07-18 19:14:23.415352+00
7	auth	0004_alter_user_username_opts	2022-07-18 19:14:23.420751+00
8	auth	0005_alter_user_last_login_null	2022-07-18 19:14:23.425531+00
9	auth	0006_require_contenttypes_0002	2022-07-18 19:14:23.428608+00
10	auth	0007_alter_validators_add_error_messages	2022-07-18 19:14:23.434703+00
11	auth	0008_alter_user_username_max_length	2022-07-18 19:14:23.442176+00
12	auth	0009_alter_user_last_name_max_length	2022-07-18 19:14:23.448584+00
13	auth	0010_alter_group_name_max_length	2022-07-18 19:14:23.456094+00
14	auth	0011_update_proxy_permissions	2022-07-18 19:14:23.464034+00
15	auth	0012_alter_user_first_name_max_length	2022-07-18 19:14:23.469356+00
16	users	0001_initial	2022-07-18 19:14:23.544129+00
17	admin	0001_initial	2022-07-18 19:14:23.561032+00
18	admin	0002_logentry_remove_auto_add	2022-07-18 19:14:23.568877+00
19	admin	0003_logentry_add_action_flag_choices	2022-07-18 19:14:23.577875+00
20	feedback	0001_initial	2022-07-18 19:14:23.593338+00
21	feedback	0002_initial	2022-07-18 19:14:23.608602+00
22	messaging	0001_initial	2022-07-18 19:14:23.62351+00
23	messaging	0002_initial	2022-07-18 19:14:23.709889+00
24	reporting	0001_initial	2022-07-18 19:14:23.7277+00
25	reporting	0002_initial	2022-07-18 19:14:23.746368+00
26	services	0002_initial	2022-07-18 19:14:23.846335+00
27	sessions	0001_initial	2022-07-18 19:14:23.855074+00
28	users	0002_alter_user_phone_number	2022-07-18 19:41:06.234386+00
29	users	0003_expert_status	2022-07-18 20:01:27.760642+00
30	services	0003_alter_servicerequest_status	2022-07-21 08:57:29.317569+00
31	services	0004_alter_servicerequest_expert_and_more	2022-07-21 09:20:47.411479+00
32	services	0005_servicerequest_created_at	2022-07-21 09:57:59.86172+00
\.


--
-- Data for Name: django_session; Type: TABLE DATA; Schema: public; Owner: admin
--

COPY public.django_session (session_key, session_data, expire_date) FROM stdin;
rg77wuf0v5r870pya6gbegpqk7r4dtci	.eJxVjEEOwiAQRe_C2hChtAMu3XsGMswMUjU0Ke3KeHfbpAvd_vfef6uI61Li2mSOI6uLAnX63RLSU-oO-IH1Pmma6jKPSe-KPmjTt4nldT3cv4OCrWy1CcbxYExnoSfOjrj3AawXkACcoc-SyDoiAjx7O4B0uBEJ2XskB-rzBeAaODQ:1oEaGn:BrsLev0M3wmCoXTPnA9Cr9Eg-cDOJQjuHD6IXSEX_ZA	2022-08-04 17:47:29.532937+00
f2iyug55ckcffr9kuov05p5djx96yk78	.eJxVjEEOwiAQRe_C2hCZMBRcuvcMZJgBqRqalHbVeHdt0oVu_3vvbyrSutS49jzHUdRFoTr9bon4mdsO5EHtPmme2jKPSe-KPmjXt0ny63q4fweVev3WDN6B8Q4dMNviIGHCUorNIsCCjskCsvcSxAycKZhAwxnJGDTWF_X-AO3NOA4:1oFIJM:TDbmbZlsDi28jx-KtBuwfztf5SwYpVoZU9XwALl-5Ps	2022-08-06 16:49:04.319947+00
r2s43z9ucfdb7en657hkk6hw4w1jsidb	.eJxVjEEOgjAQRe_StWmmpQzVpXvO0Mx0BkENTSisjHdXEha6_e-9_zKJtnVMW9UlTWIuxpvT78aUHzrvQO4034rNZV6Xie2u2INW2xfR5_Vw_w5GquO3Jp8RAwVAEXZC2SE00DIM6H2Mwl0eOm6UFFRi6zCGs6AbFJA7D2reH-5pOB4:1oJxjZ:oLUAHGWGB5Wj1rJnG2WsxhXca0iLfES8QGCv_AvYF4k	2022-08-19 13:51:25.170621+00
ygix1985obw2wuyxtwk3a660q1n2jp1m	.eJxVjEEOwiAQRe_C2hCZMBRcuvcMZJgBqRqalHbVeHdt0oVu_3vvbyrSutS49jzHUdRFoTr9bon4mdsO5EHtPmme2jKPSe-KPmjXt0ny63q4fweVev3WDN6B8Q4dMNviIGHCUorNIsCCjskCsvcSxAycKZhAwxnJGDTWF_X-AO3NOA4:1oESmH:RBcVZRGoQY2_PkuoCrfbI3uReoeoyAdkvGLev6TTOys	2022-08-04 09:47:29.242275+00
p2sxuj6hqq5zjyt0njw66294tr2xjh28	.eJxVjDEOwjAMRe-SGUWtgw1hZOcMkZ04pIBSqWknxN1ppQ6w_vfef5vAy1zC0nQKQzIXQ-bwuwnHp9YNpAfX-2jjWOdpELspdqfN3sakr-vu_h0UbmWtwUWUCNTntcmsQMcE2LkkwgQaPWTkntD7c84OO0FPRJoRJKnAyXy-BNg4kw:1oESmV:tUc6ovJUZxDQ6xx3uj1oshs20AKDVslFIVoswsqCEJ4	2022-08-04 09:47:43.304508+00
90ae5djgsx0psw7bavyfskqibib07en0	.eJxVjEEOwiAQRe_C2hChtAMu3XsGMswMUjU0Ke3KeHfbpAvd_vfef6uI61Li2mSOI6uLAnX63RLSU-oO-IH1Pmma6jKPSe-KPmjTt4nldT3cv4OCrWy1CcbxYExnoSfOjrj3AawXkACcoc-SyDoiAjx7O4B0uBEJ2XskB-rzBeAaODQ:1oESqL:n8smGq4xUVXFNJ59paOknge8o0ofoOcL51avInavgI0	2022-08-04 09:51:41.005585+00
\.


--
-- Data for Name: feedback_evaluationfeedback; Type: TABLE DATA; Schema: public; Owner: admin
--

COPY public.feedback_evaluationfeedback (id, rate, evaluation_metric_id, feedback_id) FROM stdin;
\.


--
-- Data for Name: feedback_evaluationmetric; Type: TABLE DATA; Schema: public; Owner: admin
--

COPY public.feedback_evaluationmetric (id, question, hidden) FROM stdin;
\.


--
-- Data for Name: feedback_feedback; Type: TABLE DATA; Schema: public; Owner: admin
--

COPY public.feedback_feedback (id, time_of_completion, customer_description, service_request_id) FROM stdin;
\.


--
-- Data for Name: messaging_message; Type: TABLE DATA; Schema: public; Owner: admin
--

COPY public.messaging_message (id, time_of_creation, customer_id, expert_id, related_service_request_id) FROM stdin;
\.


--
-- Data for Name: messaging_messagecontent; Type: TABLE DATA; Schema: public; Owner: admin
--

COPY public.messaging_messagecontent (id, "time", text, file, parent_message_id, sender_id) FROM stdin;
\.


--
-- Data for Name: messaging_ticket; Type: TABLE DATA; Schema: public; Owner: admin
--

COPY public.messaging_ticket (id, topic, time_of_creation, status, creator_id) FROM stdin;
\.


--
-- Data for Name: messaging_ticketmessage; Type: TABLE DATA; Schema: public; Owner: admin
--

COPY public.messaging_ticketmessage (id, text, file, "time", sender_id, ticket_id) FROM stdin;
\.


--
-- Data for Name: reporting_reportrequest; Type: TABLE DATA; Schema: public; Owner: admin
--

COPY public.reporting_reportrequest (id, start_time, end_time, report_type, report_sort_type, request_initiator_id) FROM stdin;
\.


--
-- Data for Name: reporting_reportresponse; Type: TABLE DATA; Schema: public; Owner: admin
--

COPY public.reporting_reportresponse (id, status, result_type, result, request_id) FROM stdin;
\.


--
-- Data for Name: services_requestrejectionrelation; Type: TABLE DATA; Schema: public; Owner: admin
--

COPY public.services_requestrejectionrelation (id, expert_id, request_id) FROM stdin;
12	6	35
13	7	36
14	6	38
\.


--
-- Data for Name: services_service; Type: TABLE DATA; Schema: public; Owner: admin
--

COPY public.services_service (id, name, description, category_id) FROM stdin;
1	نظافت میز	نظافت میز	2
2	تعمیر ظرف‌شویی	تعمیر ظرف‌شویی	4
3	تعمیر آنتن	تعمیر آنتن	7
\.


--
-- Data for Name: services_servicecategory; Type: TABLE DATA; Schema: public; Owner: admin
--

COPY public.services_servicecategory (id, name, description, parent_id) FROM stdin;
1	حمل و نقل	حمل و نقل	\N
2	نظافت	نظافت	\N
3	فنی	فنی	\N
4	آشپزخانه	آشپزخانه	3
7	تلویزیون	تلویزیون	3
\.


--
-- Data for Name: services_servicerequest; Type: TABLE DATA; Schema: public; Owner: admin
--

COPY public.services_servicerequest (id, status, request_type, customer_id, expert_id, service_id, created_at) FROM stdin;
35	FINISHED	SYSTEM_SELECTED	2	5	1	2022-07-23 16:06:20.988824+00
36	CANCELED_BY_EXPERT	CUSTOMER_SELECTED	4	7	2	2022-07-23 16:07:37.325177+00
37	FINISHED	CUSTOMER_SELECTED	2	7	2	2022-07-23 16:44:33.601512+00
38	FINISHED	SYSTEM_SELECTED	2	5	1	2022-07-23 16:46:09.026983+00
34	FINISHED	SYSTEM_SELECTED	2	6	1	2022-07-23 16:05:53.634063+00
\.


--
-- Data for Name: users_customer; Type: TABLE DATA; Schema: public; Owner: admin
--

COPY public.users_customer (role_ptr_id, address) FROM stdin;
1	تهران. شریف
2	تهران. شریف
4	تهران. مازندران
9	تهران، خیابان آزادی
\.


--
-- Data for Name: users_expert; Type: TABLE DATA; Schema: public; Owner: admin
--

COPY public.users_expert (role_ptr_id, document, expertise_id, status) FROM stdin;
6	documents/2022/07/18/ورود1.png	1	t
7	documents/2022/07/21/مشاهده_لیست_خدمات_و_درخواست_خدمت.png	2	t
8	documents/2022/07/21/ورود3.png	3	t
5	documents/2022/07/18/ورود2.png	1	f
3	documents/2022/07/18/ورود_به_پنل_ادمین.png	2	t
\.


--
-- Data for Name: users_itmanager; Type: TABLE DATA; Schema: public; Owner: admin
--

COPY public.users_itmanager (role_ptr_id) FROM stdin;
\.


--
-- Data for Name: users_manager; Type: TABLE DATA; Schema: public; Owner: admin
--

COPY public.users_manager (role_ptr_id) FROM stdin;
\.


--
-- Data for Name: users_role; Type: TABLE DATA; Schema: public; Owner: admin
--

COPY public.users_role (id, name, polymorphic_ctype_id) FROM stdin;
1	Role	10
2	Role	10
4	Role	10
6	Role	14
7	Role	14
9	Role	10
8	Role	14
5	Role	14
3	Role	14
\.


--
-- Data for Name: users_user; Type: TABLE DATA; Schema: public; Owner: admin
--

COPY public.users_user (id, password, last_login, is_superuser, first_name, last_name, is_staff, is_active, date_joined, username, email, phone_number, name, role_id) FROM stdin;
3	pbkdf2_sha256$320000$NJn9hOoQ62Skd3FDwyX9ps$MFjxkpaMHi0AnxprlsaAEUml+X56FOph6pdYzof8qZ4=	2022-07-28 21:56:06.404127+00	f			f	t	2022-07-18 19:50:12.012958+00	expert	mohsendehghankar2@gmail.com	09119901147	سجاد ریحانی	3
2	pbkdf2_sha256$320000$8dTR5KElGHtaWd75SeLYi3$RrUzlzXGICWGw2FYVAL2fixFIHEEDvbZ8vTLoDLlbAU=	2022-08-05 13:51:25.155694+00	f			f	t	2022-07-18 19:41:16.125736+00	customer	mohsendehghankar@gmail.com	09119901137	محسن دهقانکار	2
4	pbkdf2_sha256$320000$GWTPRAdmJacFaVHAfaMzH6$XeEJ6CF7EChQUZ37mU1mTaacHmEidBDwlk4Y5BMrUCk=	2022-07-23 16:07:30.829404+00	f			f	t	2022-07-18 19:55:16.50699+00	customer2	mohsen.dehghankar@sharif.edu	09119901145	محسن دهقانکار	4
8	pbkdf2_sha256$320000$QNhVnDpLawBQWA2vyjdzaz$ffhcW1p5HyKsBo/OAMNE+piq3hufjHkqyzF6hETX4OM=	2022-07-21 17:49:53.877788+00	f			f	t	2022-07-21 17:48:54.461408+00	expert5	m.sdfasd@gmail.com	09123452020	محمد محمدی	8
9	pbkdf2_sha256$320000$StMmwKSMUUErPCX7eEGOs2$Bf7665JBUZed6r7R8E8Iw1H8lNU/C7w0KLT7mUCLMMU=	2022-07-21 17:52:58.410561+00	f			f	t	2022-07-21 17:49:31.55937+00	customer3	mdnrmdnr@gmail.com	09321233422	مشتری مشتری‌ای	9
6	pbkdf2_sha256$320000$mHT7C3n2gYOhtDgBgcXj5Y$5ynpvjoUKnUf2+HbmA9gB4rPd5BOckA5GRyGlVtRuQg=	2022-07-23 16:48:34.109622+00	f			f	t	2022-07-18 20:02:08.129815+00	expert3	r1014@gmail.com	09119901149	محمد احمدی	6
1	pbkdf2_sha256$320000$vBUtYhZ6ngbkevC4cMvdoW$QlH7Z9Vp6XATr40uc8aUnQHfCgrOxjA75glKSUX6QHg=	2022-07-23 16:48:47.836086+00	t			t	t	2022-07-18 19:14:50.688774+00	admin	m.dehghankar@outlook.com		no name	\N
5	pbkdf2_sha256$320000$Aq3HLXgVLp4Vj6pS6RoQpj$ylnSL6HMLqKMYe5x0NlrzEZNP6K6Jp5Bq46KIYkjtc0=	2022-07-23 16:49:04.318531+00	f			f	t	2022-07-18 19:55:46.634094+00	expert2	salam@gmail.com	09119901168	محسن دهقان کار	5
7	pbkdf2_sha256$320000$fx4l25IE7DBfhBy8IoJUts$eE7mJ/+O5GWRWISbqQVVxxjLiq+rLxmBaOj/8l3Gm6U=	2022-07-23 16:56:15.976607+00	f			f	t	2022-07-21 08:56:26.145858+00	expert4	rezasdfamosavi@gmail.com	09119901130	سپهر صفری	7
\.


--
-- Data for Name: users_user_groups; Type: TABLE DATA; Schema: public; Owner: admin
--

COPY public.users_user_groups (id, user_id, group_id) FROM stdin;
\.


--
-- Data for Name: users_user_user_permissions; Type: TABLE DATA; Schema: public; Owner: admin
--

COPY public.users_user_user_permissions (id, user_id, permission_id) FROM stdin;
\.


--
-- Name: auth_group_id_seq; Type: SEQUENCE SET; Schema: public; Owner: admin
--

SELECT pg_catalog.setval('public.auth_group_id_seq', 1, false);


--
-- Name: auth_group_permissions_id_seq; Type: SEQUENCE SET; Schema: public; Owner: admin
--

SELECT pg_catalog.setval('public.auth_group_permissions_id_seq', 1, false);


--
-- Name: auth_permission_id_seq; Type: SEQUENCE SET; Schema: public; Owner: admin
--

SELECT pg_catalog.setval('public.auth_permission_id_seq', 96, true);


--
-- Name: django_admin_log_id_seq; Type: SEQUENCE SET; Schema: public; Owner: admin
--

SELECT pg_catalog.setval('public.django_admin_log_id_seq', 42, true);


--
-- Name: django_content_type_id_seq; Type: SEQUENCE SET; Schema: public; Owner: admin
--

SELECT pg_catalog.setval('public.django_content_type_id_seq', 24, true);


--
-- Name: django_migrations_id_seq; Type: SEQUENCE SET; Schema: public; Owner: admin
--

SELECT pg_catalog.setval('public.django_migrations_id_seq', 32, true);


--
-- Name: feedback_evaluationfeedback_id_seq; Type: SEQUENCE SET; Schema: public; Owner: admin
--

SELECT pg_catalog.setval('public.feedback_evaluationfeedback_id_seq', 1, false);


--
-- Name: feedback_evaluationmetric_id_seq; Type: SEQUENCE SET; Schema: public; Owner: admin
--

SELECT pg_catalog.setval('public.feedback_evaluationmetric_id_seq', 1, false);


--
-- Name: feedback_feedback_id_seq; Type: SEQUENCE SET; Schema: public; Owner: admin
--

SELECT pg_catalog.setval('public.feedback_feedback_id_seq', 1, false);


--
-- Name: messaging_message_id_seq; Type: SEQUENCE SET; Schema: public; Owner: admin
--

SELECT pg_catalog.setval('public.messaging_message_id_seq', 1, false);


--
-- Name: messaging_messagecontent_id_seq; Type: SEQUENCE SET; Schema: public; Owner: admin
--

SELECT pg_catalog.setval('public.messaging_messagecontent_id_seq', 1, false);


--
-- Name: messaging_ticket_id_seq; Type: SEQUENCE SET; Schema: public; Owner: admin
--

SELECT pg_catalog.setval('public.messaging_ticket_id_seq', 1, false);


--
-- Name: messaging_ticketmessage_id_seq; Type: SEQUENCE SET; Schema: public; Owner: admin
--

SELECT pg_catalog.setval('public.messaging_ticketmessage_id_seq', 1, false);


--
-- Name: reporting_reportrequest_id_seq; Type: SEQUENCE SET; Schema: public; Owner: admin
--

SELECT pg_catalog.setval('public.reporting_reportrequest_id_seq', 1, false);


--
-- Name: reporting_reportresponse_id_seq; Type: SEQUENCE SET; Schema: public; Owner: admin
--

SELECT pg_catalog.setval('public.reporting_reportresponse_id_seq', 1, false);


--
-- Name: services_requestrejectionrelation_id_seq; Type: SEQUENCE SET; Schema: public; Owner: admin
--

SELECT pg_catalog.setval('public.services_requestrejectionrelation_id_seq', 14, true);


--
-- Name: services_service_id_seq; Type: SEQUENCE SET; Schema: public; Owner: admin
--

SELECT pg_catalog.setval('public.services_service_id_seq', 3, true);


--
-- Name: services_servicecategory_id_seq; Type: SEQUENCE SET; Schema: public; Owner: admin
--

SELECT pg_catalog.setval('public.services_servicecategory_id_seq', 7, true);


--
-- Name: services_servicerequest_id_seq; Type: SEQUENCE SET; Schema: public; Owner: admin
--

SELECT pg_catalog.setval('public.services_servicerequest_id_seq', 38, true);


--
-- Name: users_role_id_seq; Type: SEQUENCE SET; Schema: public; Owner: admin
--

SELECT pg_catalog.setval('public.users_role_id_seq', 9, true);


--
-- Name: users_user_groups_id_seq; Type: SEQUENCE SET; Schema: public; Owner: admin
--

SELECT pg_catalog.setval('public.users_user_groups_id_seq', 1, false);


--
-- Name: users_user_id_seq; Type: SEQUENCE SET; Schema: public; Owner: admin
--

SELECT pg_catalog.setval('public.users_user_id_seq', 9, true);


--
-- Name: users_user_user_permissions_id_seq; Type: SEQUENCE SET; Schema: public; Owner: admin
--

SELECT pg_catalog.setval('public.users_user_user_permissions_id_seq', 1, false);


--
-- Name: auth_group auth_group_name_key; Type: CONSTRAINT; Schema: public; Owner: admin
--

ALTER TABLE ONLY public.auth_group
    ADD CONSTRAINT auth_group_name_key UNIQUE (name);


--
-- Name: auth_group_permissions auth_group_permissions_group_id_permission_id_0cd325b0_uniq; Type: CONSTRAINT; Schema: public; Owner: admin
--

ALTER TABLE ONLY public.auth_group_permissions
    ADD CONSTRAINT auth_group_permissions_group_id_permission_id_0cd325b0_uniq UNIQUE (group_id, permission_id);


--
-- Name: auth_group_permissions auth_group_permissions_pkey; Type: CONSTRAINT; Schema: public; Owner: admin
--

ALTER TABLE ONLY public.auth_group_permissions
    ADD CONSTRAINT auth_group_permissions_pkey PRIMARY KEY (id);


--
-- Name: auth_group auth_group_pkey; Type: CONSTRAINT; Schema: public; Owner: admin
--

ALTER TABLE ONLY public.auth_group
    ADD CONSTRAINT auth_group_pkey PRIMARY KEY (id);


--
-- Name: auth_permission auth_permission_content_type_id_codename_01ab375a_uniq; Type: CONSTRAINT; Schema: public; Owner: admin
--

ALTER TABLE ONLY public.auth_permission
    ADD CONSTRAINT auth_permission_content_type_id_codename_01ab375a_uniq UNIQUE (content_type_id, codename);


--
-- Name: auth_permission auth_permission_pkey; Type: CONSTRAINT; Schema: public; Owner: admin
--

ALTER TABLE ONLY public.auth_permission
    ADD CONSTRAINT auth_permission_pkey PRIMARY KEY (id);


--
-- Name: django_admin_log django_admin_log_pkey; Type: CONSTRAINT; Schema: public; Owner: admin
--

ALTER TABLE ONLY public.django_admin_log
    ADD CONSTRAINT django_admin_log_pkey PRIMARY KEY (id);


--
-- Name: django_content_type django_content_type_app_label_model_76bd3d3b_uniq; Type: CONSTRAINT; Schema: public; Owner: admin
--

ALTER TABLE ONLY public.django_content_type
    ADD CONSTRAINT django_content_type_app_label_model_76bd3d3b_uniq UNIQUE (app_label, model);


--
-- Name: django_content_type django_content_type_pkey; Type: CONSTRAINT; Schema: public; Owner: admin
--

ALTER TABLE ONLY public.django_content_type
    ADD CONSTRAINT django_content_type_pkey PRIMARY KEY (id);


--
-- Name: django_migrations django_migrations_pkey; Type: CONSTRAINT; Schema: public; Owner: admin
--

ALTER TABLE ONLY public.django_migrations
    ADD CONSTRAINT django_migrations_pkey PRIMARY KEY (id);


--
-- Name: django_session django_session_pkey; Type: CONSTRAINT; Schema: public; Owner: admin
--

ALTER TABLE ONLY public.django_session
    ADD CONSTRAINT django_session_pkey PRIMARY KEY (session_key);


--
-- Name: feedback_evaluationfeedback feedback_evaluationfeedback_pkey; Type: CONSTRAINT; Schema: public; Owner: admin
--

ALTER TABLE ONLY public.feedback_evaluationfeedback
    ADD CONSTRAINT feedback_evaluationfeedback_pkey PRIMARY KEY (id);


--
-- Name: feedback_evaluationmetric feedback_evaluationmetric_pkey; Type: CONSTRAINT; Schema: public; Owner: admin
--

ALTER TABLE ONLY public.feedback_evaluationmetric
    ADD CONSTRAINT feedback_evaluationmetric_pkey PRIMARY KEY (id);


--
-- Name: feedback_feedback feedback_feedback_pkey; Type: CONSTRAINT; Schema: public; Owner: admin
--

ALTER TABLE ONLY public.feedback_feedback
    ADD CONSTRAINT feedback_feedback_pkey PRIMARY KEY (id);


--
-- Name: messaging_message messaging_message_pkey; Type: CONSTRAINT; Schema: public; Owner: admin
--

ALTER TABLE ONLY public.messaging_message
    ADD CONSTRAINT messaging_message_pkey PRIMARY KEY (id);


--
-- Name: messaging_messagecontent messaging_messagecontent_pkey; Type: CONSTRAINT; Schema: public; Owner: admin
--

ALTER TABLE ONLY public.messaging_messagecontent
    ADD CONSTRAINT messaging_messagecontent_pkey PRIMARY KEY (id);


--
-- Name: messaging_ticket messaging_ticket_pkey; Type: CONSTRAINT; Schema: public; Owner: admin
--

ALTER TABLE ONLY public.messaging_ticket
    ADD CONSTRAINT messaging_ticket_pkey PRIMARY KEY (id);


--
-- Name: messaging_ticketmessage messaging_ticketmessage_pkey; Type: CONSTRAINT; Schema: public; Owner: admin
--

ALTER TABLE ONLY public.messaging_ticketmessage
    ADD CONSTRAINT messaging_ticketmessage_pkey PRIMARY KEY (id);


--
-- Name: reporting_reportrequest reporting_reportrequest_pkey; Type: CONSTRAINT; Schema: public; Owner: admin
--

ALTER TABLE ONLY public.reporting_reportrequest
    ADD CONSTRAINT reporting_reportrequest_pkey PRIMARY KEY (id);


--
-- Name: reporting_reportresponse reporting_reportresponse_pkey; Type: CONSTRAINT; Schema: public; Owner: admin
--

ALTER TABLE ONLY public.reporting_reportresponse
    ADD CONSTRAINT reporting_reportresponse_pkey PRIMARY KEY (id);


--
-- Name: services_requestrejectionrelation services_requestrejectionrelation_pkey; Type: CONSTRAINT; Schema: public; Owner: admin
--

ALTER TABLE ONLY public.services_requestrejectionrelation
    ADD CONSTRAINT services_requestrejectionrelation_pkey PRIMARY KEY (id);


--
-- Name: services_service services_service_pkey; Type: CONSTRAINT; Schema: public; Owner: admin
--

ALTER TABLE ONLY public.services_service
    ADD CONSTRAINT services_service_pkey PRIMARY KEY (id);


--
-- Name: services_servicecategory services_servicecategory_pkey; Type: CONSTRAINT; Schema: public; Owner: admin
--

ALTER TABLE ONLY public.services_servicecategory
    ADD CONSTRAINT services_servicecategory_pkey PRIMARY KEY (id);


--
-- Name: services_servicerequest services_servicerequest_pkey; Type: CONSTRAINT; Schema: public; Owner: admin
--

ALTER TABLE ONLY public.services_servicerequest
    ADD CONSTRAINT services_servicerequest_pkey PRIMARY KEY (id);


--
-- Name: users_customer users_customer_pkey; Type: CONSTRAINT; Schema: public; Owner: admin
--

ALTER TABLE ONLY public.users_customer
    ADD CONSTRAINT users_customer_pkey PRIMARY KEY (role_ptr_id);


--
-- Name: users_expert users_expert_pkey; Type: CONSTRAINT; Schema: public; Owner: admin
--

ALTER TABLE ONLY public.users_expert
    ADD CONSTRAINT users_expert_pkey PRIMARY KEY (role_ptr_id);


--
-- Name: users_itmanager users_itmanager_pkey; Type: CONSTRAINT; Schema: public; Owner: admin
--

ALTER TABLE ONLY public.users_itmanager
    ADD CONSTRAINT users_itmanager_pkey PRIMARY KEY (role_ptr_id);


--
-- Name: users_manager users_manager_pkey; Type: CONSTRAINT; Schema: public; Owner: admin
--

ALTER TABLE ONLY public.users_manager
    ADD CONSTRAINT users_manager_pkey PRIMARY KEY (role_ptr_id);


--
-- Name: users_role users_role_pkey; Type: CONSTRAINT; Schema: public; Owner: admin
--

ALTER TABLE ONLY public.users_role
    ADD CONSTRAINT users_role_pkey PRIMARY KEY (id);


--
-- Name: users_user users_user_email_key; Type: CONSTRAINT; Schema: public; Owner: admin
--

ALTER TABLE ONLY public.users_user
    ADD CONSTRAINT users_user_email_key UNIQUE (email);


--
-- Name: users_user_groups users_user_groups_pkey; Type: CONSTRAINT; Schema: public; Owner: admin
--

ALTER TABLE ONLY public.users_user_groups
    ADD CONSTRAINT users_user_groups_pkey PRIMARY KEY (id);


--
-- Name: users_user_groups users_user_groups_user_id_group_id_b88eab82_uniq; Type: CONSTRAINT; Schema: public; Owner: admin
--

ALTER TABLE ONLY public.users_user_groups
    ADD CONSTRAINT users_user_groups_user_id_group_id_b88eab82_uniq UNIQUE (user_id, group_id);


--
-- Name: users_user users_user_pkey; Type: CONSTRAINT; Schema: public; Owner: admin
--

ALTER TABLE ONLY public.users_user
    ADD CONSTRAINT users_user_pkey PRIMARY KEY (id);


--
-- Name: users_user_user_permissions users_user_user_permissions_pkey; Type: CONSTRAINT; Schema: public; Owner: admin
--

ALTER TABLE ONLY public.users_user_user_permissions
    ADD CONSTRAINT users_user_user_permissions_pkey PRIMARY KEY (id);


--
-- Name: users_user_user_permissions users_user_user_permissions_user_id_permission_id_43338c45_uniq; Type: CONSTRAINT; Schema: public; Owner: admin
--

ALTER TABLE ONLY public.users_user_user_permissions
    ADD CONSTRAINT users_user_user_permissions_user_id_permission_id_43338c45_uniq UNIQUE (user_id, permission_id);


--
-- Name: users_user users_user_username_key; Type: CONSTRAINT; Schema: public; Owner: admin
--

ALTER TABLE ONLY public.users_user
    ADD CONSTRAINT users_user_username_key UNIQUE (username);


--
-- Name: auth_group_name_a6ea08ec_like; Type: INDEX; Schema: public; Owner: admin
--

CREATE INDEX auth_group_name_a6ea08ec_like ON public.auth_group USING btree (name varchar_pattern_ops);


--
-- Name: auth_group_permissions_group_id_b120cbf9; Type: INDEX; Schema: public; Owner: admin
--

CREATE INDEX auth_group_permissions_group_id_b120cbf9 ON public.auth_group_permissions USING btree (group_id);


--
-- Name: auth_group_permissions_permission_id_84c5c92e; Type: INDEX; Schema: public; Owner: admin
--

CREATE INDEX auth_group_permissions_permission_id_84c5c92e ON public.auth_group_permissions USING btree (permission_id);


--
-- Name: auth_permission_content_type_id_2f476e4b; Type: INDEX; Schema: public; Owner: admin
--

CREATE INDEX auth_permission_content_type_id_2f476e4b ON public.auth_permission USING btree (content_type_id);


--
-- Name: django_admin_log_content_type_id_c4bce8eb; Type: INDEX; Schema: public; Owner: admin
--

CREATE INDEX django_admin_log_content_type_id_c4bce8eb ON public.django_admin_log USING btree (content_type_id);


--
-- Name: django_admin_log_user_id_c564eba6; Type: INDEX; Schema: public; Owner: admin
--

CREATE INDEX django_admin_log_user_id_c564eba6 ON public.django_admin_log USING btree (user_id);


--
-- Name: django_session_expire_date_a5c62663; Type: INDEX; Schema: public; Owner: admin
--

CREATE INDEX django_session_expire_date_a5c62663 ON public.django_session USING btree (expire_date);


--
-- Name: django_session_session_key_c0390e0f_like; Type: INDEX; Schema: public; Owner: admin
--

CREATE INDEX django_session_session_key_c0390e0f_like ON public.django_session USING btree (session_key varchar_pattern_ops);


--
-- Name: feedback_evaluationfeedback_evaluation_metric_id_4e46a334; Type: INDEX; Schema: public; Owner: admin
--

CREATE INDEX feedback_evaluationfeedback_evaluation_metric_id_4e46a334 ON public.feedback_evaluationfeedback USING btree (evaluation_metric_id);


--
-- Name: feedback_evaluationfeedback_feedback_id_b189355b; Type: INDEX; Schema: public; Owner: admin
--

CREATE INDEX feedback_evaluationfeedback_feedback_id_b189355b ON public.feedback_evaluationfeedback USING btree (feedback_id);


--
-- Name: feedback_feedback_service_request_id_9b30e06e; Type: INDEX; Schema: public; Owner: admin
--

CREATE INDEX feedback_feedback_service_request_id_9b30e06e ON public.feedback_feedback USING btree (service_request_id);


--
-- Name: messaging_message_customer_id_8d410b21; Type: INDEX; Schema: public; Owner: admin
--

CREATE INDEX messaging_message_customer_id_8d410b21 ON public.messaging_message USING btree (customer_id);


--
-- Name: messaging_message_expert_id_a9b5dc31; Type: INDEX; Schema: public; Owner: admin
--

CREATE INDEX messaging_message_expert_id_a9b5dc31 ON public.messaging_message USING btree (expert_id);


--
-- Name: messaging_message_related_service_request_id_7fa32e5d; Type: INDEX; Schema: public; Owner: admin
--

CREATE INDEX messaging_message_related_service_request_id_7fa32e5d ON public.messaging_message USING btree (related_service_request_id);


--
-- Name: messaging_messagecontent_parent_message_id_5527be1b; Type: INDEX; Schema: public; Owner: admin
--

CREATE INDEX messaging_messagecontent_parent_message_id_5527be1b ON public.messaging_messagecontent USING btree (parent_message_id);


--
-- Name: messaging_messagecontent_sender_id_8a538a67; Type: INDEX; Schema: public; Owner: admin
--

CREATE INDEX messaging_messagecontent_sender_id_8a538a67 ON public.messaging_messagecontent USING btree (sender_id);


--
-- Name: messaging_ticket_creator_id_c487f8a6; Type: INDEX; Schema: public; Owner: admin
--

CREATE INDEX messaging_ticket_creator_id_c487f8a6 ON public.messaging_ticket USING btree (creator_id);


--
-- Name: messaging_ticketmessage_sender_id_d7768f44; Type: INDEX; Schema: public; Owner: admin
--

CREATE INDEX messaging_ticketmessage_sender_id_d7768f44 ON public.messaging_ticketmessage USING btree (sender_id);


--
-- Name: messaging_ticketmessage_ticket_id_651cbc38; Type: INDEX; Schema: public; Owner: admin
--

CREATE INDEX messaging_ticketmessage_ticket_id_651cbc38 ON public.messaging_ticketmessage USING btree (ticket_id);


--
-- Name: reporting_reportrequest_request_initiator_id_a0a692f8; Type: INDEX; Schema: public; Owner: admin
--

CREATE INDEX reporting_reportrequest_request_initiator_id_a0a692f8 ON public.reporting_reportrequest USING btree (request_initiator_id);


--
-- Name: reporting_reportresponse_request_id_698e164d; Type: INDEX; Schema: public; Owner: admin
--

CREATE INDEX reporting_reportresponse_request_id_698e164d ON public.reporting_reportresponse USING btree (request_id);


--
-- Name: services_requestrejectionrelation_expert_id_40edef32; Type: INDEX; Schema: public; Owner: admin
--

CREATE INDEX services_requestrejectionrelation_expert_id_40edef32 ON public.services_requestrejectionrelation USING btree (expert_id);


--
-- Name: services_requestrejectionrelation_request_id_4386451d; Type: INDEX; Schema: public; Owner: admin
--

CREATE INDEX services_requestrejectionrelation_request_id_4386451d ON public.services_requestrejectionrelation USING btree (request_id);


--
-- Name: services_service_category_id_e15f8b7e; Type: INDEX; Schema: public; Owner: admin
--

CREATE INDEX services_service_category_id_e15f8b7e ON public.services_service USING btree (category_id);


--
-- Name: services_servicecategory_parent_id_a129700f; Type: INDEX; Schema: public; Owner: admin
--

CREATE INDEX services_servicecategory_parent_id_a129700f ON public.services_servicecategory USING btree (parent_id);


--
-- Name: services_servicerequest_customer_id_4e375274; Type: INDEX; Schema: public; Owner: admin
--

CREATE INDEX services_servicerequest_customer_id_4e375274 ON public.services_servicerequest USING btree (customer_id);


--
-- Name: services_servicerequest_expert_id_a0d091bd; Type: INDEX; Schema: public; Owner: admin
--

CREATE INDEX services_servicerequest_expert_id_a0d091bd ON public.services_servicerequest USING btree (expert_id);


--
-- Name: services_servicerequest_service_id_b9613175; Type: INDEX; Schema: public; Owner: admin
--

CREATE INDEX services_servicerequest_service_id_b9613175 ON public.services_servicerequest USING btree (service_id);


--
-- Name: users_expert_expertise_id_c6fe456d; Type: INDEX; Schema: public; Owner: admin
--

CREATE INDEX users_expert_expertise_id_c6fe456d ON public.users_expert USING btree (expertise_id);


--
-- Name: users_role_polymorphic_ctype_id_6caa4f27; Type: INDEX; Schema: public; Owner: admin
--

CREATE INDEX users_role_polymorphic_ctype_id_6caa4f27 ON public.users_role USING btree (polymorphic_ctype_id);


--
-- Name: users_user_email_243f6e77_like; Type: INDEX; Schema: public; Owner: admin
--

CREATE INDEX users_user_email_243f6e77_like ON public.users_user USING btree (email varchar_pattern_ops);


--
-- Name: users_user_groups_group_id_9afc8d0e; Type: INDEX; Schema: public; Owner: admin
--

CREATE INDEX users_user_groups_group_id_9afc8d0e ON public.users_user_groups USING btree (group_id);


--
-- Name: users_user_groups_user_id_5f6f5a90; Type: INDEX; Schema: public; Owner: admin
--

CREATE INDEX users_user_groups_user_id_5f6f5a90 ON public.users_user_groups USING btree (user_id);


--
-- Name: users_user_role_id_854f2687; Type: INDEX; Schema: public; Owner: admin
--

CREATE INDEX users_user_role_id_854f2687 ON public.users_user USING btree (role_id);


--
-- Name: users_user_user_permissions_permission_id_0b93982e; Type: INDEX; Schema: public; Owner: admin
--

CREATE INDEX users_user_user_permissions_permission_id_0b93982e ON public.users_user_user_permissions USING btree (permission_id);


--
-- Name: users_user_user_permissions_user_id_20aca447; Type: INDEX; Schema: public; Owner: admin
--

CREATE INDEX users_user_user_permissions_user_id_20aca447 ON public.users_user_user_permissions USING btree (user_id);


--
-- Name: users_user_username_06e46fe6_like; Type: INDEX; Schema: public; Owner: admin
--

CREATE INDEX users_user_username_06e46fe6_like ON public.users_user USING btree (username varchar_pattern_ops);


--
-- Name: auth_group_permissions auth_group_permissio_permission_id_84c5c92e_fk_auth_perm; Type: FK CONSTRAINT; Schema: public; Owner: admin
--

ALTER TABLE ONLY public.auth_group_permissions
    ADD CONSTRAINT auth_group_permissio_permission_id_84c5c92e_fk_auth_perm FOREIGN KEY (permission_id) REFERENCES public.auth_permission(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: auth_group_permissions auth_group_permissions_group_id_b120cbf9_fk_auth_group_id; Type: FK CONSTRAINT; Schema: public; Owner: admin
--

ALTER TABLE ONLY public.auth_group_permissions
    ADD CONSTRAINT auth_group_permissions_group_id_b120cbf9_fk_auth_group_id FOREIGN KEY (group_id) REFERENCES public.auth_group(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: auth_permission auth_permission_content_type_id_2f476e4b_fk_django_co; Type: FK CONSTRAINT; Schema: public; Owner: admin
--

ALTER TABLE ONLY public.auth_permission
    ADD CONSTRAINT auth_permission_content_type_id_2f476e4b_fk_django_co FOREIGN KEY (content_type_id) REFERENCES public.django_content_type(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: django_admin_log django_admin_log_content_type_id_c4bce8eb_fk_django_co; Type: FK CONSTRAINT; Schema: public; Owner: admin
--

ALTER TABLE ONLY public.django_admin_log
    ADD CONSTRAINT django_admin_log_content_type_id_c4bce8eb_fk_django_co FOREIGN KEY (content_type_id) REFERENCES public.django_content_type(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: django_admin_log django_admin_log_user_id_c564eba6_fk_users_user_id; Type: FK CONSTRAINT; Schema: public; Owner: admin
--

ALTER TABLE ONLY public.django_admin_log
    ADD CONSTRAINT django_admin_log_user_id_c564eba6_fk_users_user_id FOREIGN KEY (user_id) REFERENCES public.users_user(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: feedback_evaluationfeedback feedback_evaluationf_evaluation_metric_id_4e46a334_fk_feedback_; Type: FK CONSTRAINT; Schema: public; Owner: admin
--

ALTER TABLE ONLY public.feedback_evaluationfeedback
    ADD CONSTRAINT feedback_evaluationf_evaluation_metric_id_4e46a334_fk_feedback_ FOREIGN KEY (evaluation_metric_id) REFERENCES public.feedback_evaluationmetric(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: feedback_evaluationfeedback feedback_evaluationf_feedback_id_b189355b_fk_feedback_; Type: FK CONSTRAINT; Schema: public; Owner: admin
--

ALTER TABLE ONLY public.feedback_evaluationfeedback
    ADD CONSTRAINT feedback_evaluationf_feedback_id_b189355b_fk_feedback_ FOREIGN KEY (feedback_id) REFERENCES public.feedback_feedback(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: feedback_feedback feedback_feedback_service_request_id_9b30e06e_fk_services_; Type: FK CONSTRAINT; Schema: public; Owner: admin
--

ALTER TABLE ONLY public.feedback_feedback
    ADD CONSTRAINT feedback_feedback_service_request_id_9b30e06e_fk_services_ FOREIGN KEY (service_request_id) REFERENCES public.services_servicerequest(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: messaging_message messaging_message_customer_id_8d410b21_fk_users_cus; Type: FK CONSTRAINT; Schema: public; Owner: admin
--

ALTER TABLE ONLY public.messaging_message
    ADD CONSTRAINT messaging_message_customer_id_8d410b21_fk_users_cus FOREIGN KEY (customer_id) REFERENCES public.users_customer(role_ptr_id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: messaging_message messaging_message_expert_id_a9b5dc31_fk_users_exp; Type: FK CONSTRAINT; Schema: public; Owner: admin
--

ALTER TABLE ONLY public.messaging_message
    ADD CONSTRAINT messaging_message_expert_id_a9b5dc31_fk_users_exp FOREIGN KEY (expert_id) REFERENCES public.users_expert(role_ptr_id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: messaging_message messaging_message_related_service_requ_7fa32e5d_fk_services_; Type: FK CONSTRAINT; Schema: public; Owner: admin
--

ALTER TABLE ONLY public.messaging_message
    ADD CONSTRAINT messaging_message_related_service_requ_7fa32e5d_fk_services_ FOREIGN KEY (related_service_request_id) REFERENCES public.services_servicerequest(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: messaging_messagecontent messaging_messagecon_parent_message_id_5527be1b_fk_messaging; Type: FK CONSTRAINT; Schema: public; Owner: admin
--

ALTER TABLE ONLY public.messaging_messagecontent
    ADD CONSTRAINT messaging_messagecon_parent_message_id_5527be1b_fk_messaging FOREIGN KEY (parent_message_id) REFERENCES public.messaging_message(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: messaging_messagecontent messaging_messagecontent_sender_id_8a538a67_fk_users_user_id; Type: FK CONSTRAINT; Schema: public; Owner: admin
--

ALTER TABLE ONLY public.messaging_messagecontent
    ADD CONSTRAINT messaging_messagecontent_sender_id_8a538a67_fk_users_user_id FOREIGN KEY (sender_id) REFERENCES public.users_user(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: messaging_ticket messaging_ticket_creator_id_c487f8a6_fk_users_user_id; Type: FK CONSTRAINT; Schema: public; Owner: admin
--

ALTER TABLE ONLY public.messaging_ticket
    ADD CONSTRAINT messaging_ticket_creator_id_c487f8a6_fk_users_user_id FOREIGN KEY (creator_id) REFERENCES public.users_user(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: messaging_ticketmessage messaging_ticketmess_ticket_id_651cbc38_fk_messaging; Type: FK CONSTRAINT; Schema: public; Owner: admin
--

ALTER TABLE ONLY public.messaging_ticketmessage
    ADD CONSTRAINT messaging_ticketmess_ticket_id_651cbc38_fk_messaging FOREIGN KEY (ticket_id) REFERENCES public.messaging_ticket(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: messaging_ticketmessage messaging_ticketmessage_sender_id_d7768f44_fk_users_user_id; Type: FK CONSTRAINT; Schema: public; Owner: admin
--

ALTER TABLE ONLY public.messaging_ticketmessage
    ADD CONSTRAINT messaging_ticketmessage_sender_id_d7768f44_fk_users_user_id FOREIGN KEY (sender_id) REFERENCES public.users_user(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: reporting_reportrequest reporting_reportrequ_request_initiator_id_a0a692f8_fk_users_man; Type: FK CONSTRAINT; Schema: public; Owner: admin
--

ALTER TABLE ONLY public.reporting_reportrequest
    ADD CONSTRAINT reporting_reportrequ_request_initiator_id_a0a692f8_fk_users_man FOREIGN KEY (request_initiator_id) REFERENCES public.users_manager(role_ptr_id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: reporting_reportresponse reporting_reportresp_request_id_698e164d_fk_reporting; Type: FK CONSTRAINT; Schema: public; Owner: admin
--

ALTER TABLE ONLY public.reporting_reportresponse
    ADD CONSTRAINT reporting_reportresp_request_id_698e164d_fk_reporting FOREIGN KEY (request_id) REFERENCES public.reporting_reportrequest(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: services_requestrejectionrelation services_requestreje_expert_id_40edef32_fk_users_use; Type: FK CONSTRAINT; Schema: public; Owner: admin
--

ALTER TABLE ONLY public.services_requestrejectionrelation
    ADD CONSTRAINT services_requestreje_expert_id_40edef32_fk_users_use FOREIGN KEY (expert_id) REFERENCES public.users_user(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: services_requestrejectionrelation services_requestreje_request_id_4386451d_fk_services_; Type: FK CONSTRAINT; Schema: public; Owner: admin
--

ALTER TABLE ONLY public.services_requestrejectionrelation
    ADD CONSTRAINT services_requestreje_request_id_4386451d_fk_services_ FOREIGN KEY (request_id) REFERENCES public.services_servicerequest(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: services_service services_service_category_id_e15f8b7e_fk_services_; Type: FK CONSTRAINT; Schema: public; Owner: admin
--

ALTER TABLE ONLY public.services_service
    ADD CONSTRAINT services_service_category_id_e15f8b7e_fk_services_ FOREIGN KEY (category_id) REFERENCES public.services_servicecategory(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: services_servicecategory services_servicecate_parent_id_a129700f_fk_services_; Type: FK CONSTRAINT; Schema: public; Owner: admin
--

ALTER TABLE ONLY public.services_servicecategory
    ADD CONSTRAINT services_servicecate_parent_id_a129700f_fk_services_ FOREIGN KEY (parent_id) REFERENCES public.services_servicecategory(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: services_servicerequest services_servicerequ_service_id_b9613175_fk_services_; Type: FK CONSTRAINT; Schema: public; Owner: admin
--

ALTER TABLE ONLY public.services_servicerequest
    ADD CONSTRAINT services_servicerequ_service_id_b9613175_fk_services_ FOREIGN KEY (service_id) REFERENCES public.services_service(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: services_servicerequest services_servicerequest_customer_id_4e375274_fk_users_user_id; Type: FK CONSTRAINT; Schema: public; Owner: admin
--

ALTER TABLE ONLY public.services_servicerequest
    ADD CONSTRAINT services_servicerequest_customer_id_4e375274_fk_users_user_id FOREIGN KEY (customer_id) REFERENCES public.users_user(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: services_servicerequest services_servicerequest_expert_id_a0d091bd_fk_users_user_id; Type: FK CONSTRAINT; Schema: public; Owner: admin
--

ALTER TABLE ONLY public.services_servicerequest
    ADD CONSTRAINT services_servicerequest_expert_id_a0d091bd_fk_users_user_id FOREIGN KEY (expert_id) REFERENCES public.users_user(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: users_customer users_customer_role_ptr_id_19db9853_fk_users_role_id; Type: FK CONSTRAINT; Schema: public; Owner: admin
--

ALTER TABLE ONLY public.users_customer
    ADD CONSTRAINT users_customer_role_ptr_id_19db9853_fk_users_role_id FOREIGN KEY (role_ptr_id) REFERENCES public.users_role(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: users_expert users_expert_expertise_id_c6fe456d_fk_services_service_id; Type: FK CONSTRAINT; Schema: public; Owner: admin
--

ALTER TABLE ONLY public.users_expert
    ADD CONSTRAINT users_expert_expertise_id_c6fe456d_fk_services_service_id FOREIGN KEY (expertise_id) REFERENCES public.services_service(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: users_expert users_expert_role_ptr_id_575adbba_fk_users_role_id; Type: FK CONSTRAINT; Schema: public; Owner: admin
--

ALTER TABLE ONLY public.users_expert
    ADD CONSTRAINT users_expert_role_ptr_id_575adbba_fk_users_role_id FOREIGN KEY (role_ptr_id) REFERENCES public.users_role(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: users_itmanager users_itmanager_role_ptr_id_579487f4_fk_users_role_id; Type: FK CONSTRAINT; Schema: public; Owner: admin
--

ALTER TABLE ONLY public.users_itmanager
    ADD CONSTRAINT users_itmanager_role_ptr_id_579487f4_fk_users_role_id FOREIGN KEY (role_ptr_id) REFERENCES public.users_role(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: users_manager users_manager_role_ptr_id_364917ce_fk_users_role_id; Type: FK CONSTRAINT; Schema: public; Owner: admin
--

ALTER TABLE ONLY public.users_manager
    ADD CONSTRAINT users_manager_role_ptr_id_364917ce_fk_users_role_id FOREIGN KEY (role_ptr_id) REFERENCES public.users_role(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: users_role users_role_polymorphic_ctype_id_6caa4f27_fk_django_co; Type: FK CONSTRAINT; Schema: public; Owner: admin
--

ALTER TABLE ONLY public.users_role
    ADD CONSTRAINT users_role_polymorphic_ctype_id_6caa4f27_fk_django_co FOREIGN KEY (polymorphic_ctype_id) REFERENCES public.django_content_type(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: users_user_groups users_user_groups_group_id_9afc8d0e_fk_auth_group_id; Type: FK CONSTRAINT; Schema: public; Owner: admin
--

ALTER TABLE ONLY public.users_user_groups
    ADD CONSTRAINT users_user_groups_group_id_9afc8d0e_fk_auth_group_id FOREIGN KEY (group_id) REFERENCES public.auth_group(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: users_user_groups users_user_groups_user_id_5f6f5a90_fk_users_user_id; Type: FK CONSTRAINT; Schema: public; Owner: admin
--

ALTER TABLE ONLY public.users_user_groups
    ADD CONSTRAINT users_user_groups_user_id_5f6f5a90_fk_users_user_id FOREIGN KEY (user_id) REFERENCES public.users_user(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: users_user users_user_role_id_854f2687_fk_users_role_id; Type: FK CONSTRAINT; Schema: public; Owner: admin
--

ALTER TABLE ONLY public.users_user
    ADD CONSTRAINT users_user_role_id_854f2687_fk_users_role_id FOREIGN KEY (role_id) REFERENCES public.users_role(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: users_user_user_permissions users_user_user_perm_permission_id_0b93982e_fk_auth_perm; Type: FK CONSTRAINT; Schema: public; Owner: admin
--

ALTER TABLE ONLY public.users_user_user_permissions
    ADD CONSTRAINT users_user_user_perm_permission_id_0b93982e_fk_auth_perm FOREIGN KEY (permission_id) REFERENCES public.auth_permission(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: users_user_user_permissions users_user_user_permissions_user_id_20aca447_fk_users_user_id; Type: FK CONSTRAINT; Schema: public; Owner: admin
--

ALTER TABLE ONLY public.users_user_user_permissions
    ADD CONSTRAINT users_user_user_permissions_user_id_20aca447_fk_users_user_id FOREIGN KEY (user_id) REFERENCES public.users_user(id) DEFERRABLE INITIALLY DEFERRED;


--
-- PostgreSQL database dump complete
--

