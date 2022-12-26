create table crosslinkage
(
    ID int null,
    speciescode varchar(10),
    speciesname varchar(155),
    sub_unit varchar(255),
    assessment_code_EU int,
    assessment_specname_EU varchar(255),
    season varchar(10),
    assessment_code_trend_breeding int,
    assessment_specname_trend_breeding varchar(155),
    assessment_code_trend_wintering int,
    assessment_specname_trend_wintering varchar(155),
    addtionnal_record int

)

BULK INSERT crosslinkage FROM "../../data/crosslinkage_table.csv"
WITH(FIRSTROW = 2, FIELDTERMINATOR = ",", ROWTERMINATOR = "\n", BATCHSIZE = 25000, MAXERRORS = 8);

create table bgmeasures
(
    bgreporthash varchar(60),
    sitecode varchar(30),
    sitename varchar(300),
    project_year int,
    project_title varchar(255),
    impact varchar(255)

)

BULK INSERT bgmeasures FROM "../../data/data_bgmeasures.csv"
WITH(FIRSTROW = 2, FIELDTERMINATOR = ",", ROWTERMINATOR = "\n", BATCHSIZE = 25000, MAXERRORS = 8);

create table bgmonitoring
(
    bgreporthash varchar(60),
    monitoring_title varchar(255),
    monitoring_year int,
    monitoring_reference varchar(255)
)

BULK INSERT bgmonitoring FROM "../../data/data_bgmonitoring.csv"
WITH(FIRSTROW = 2, FIELDTERMINATOR = ",", ROWTERMINATOR = "\n", BATCHSIZE = 25000, MAXERRORS = 8);

create table bgnon_native_bird
(
    bgreporthash varchar(60),
    speciesname varchar(10),
    subspecies_name varchar(30),
    introduction varchar(60),
    consultation_date varchar(30)
)

BULK INSERT bgnon_native_bird FROM "../../data/data_bgnon_native_bird.csv"
WITH(FIRSTROW = 2, FIELDTERMINATOR = ",", ROWTERMINATOR = "\n", BATCHSIZE = 25000, MAXERRORS = 8);

create table bgpublication
(
    bgreporthash varchar(60),
    other_publication_title varchar(255),
    other_publication_year int,
    other_publication_reference varchar(255)

)

BULK INSERT bgpublication FROM "../../data/data_bgpublication.csv"
WITH(FIRSTROW = 2, FIELDTERMINATOR = ",", ROWTERMINATOR = "\n", BATCHSIZE = 25000, MAXERRORS = 8);

create table bgreport
(
    bgreporthash varchar(60),
    country varchar(10),
    country_isocode varchar(10),
    achievements varchar(255),
    achievements_trans varchar(255),
    general_information varchar(255),
    information_on_network varchar(255),
    monitoring_schemes varchar(255),
    protection_of_species varchar(255),
    transpose_directive varchar(255),
    spa_total_number int,
    spa_total_area float,
    spa_terrestrial_area float,
    spa_marine_number int,
    spa_marine_area float,
    database_date varchar(30),
    sites_with_plans int,
    coverage float,
    plans_under_prep int,
    national_bird_atlas_title varchar(60),
    national_bird_atlas_year int,
    national_bird_atlas_reference varchar(60),
    national_bird_redlist_title varchar(30),
    national_bird_redlist_year int,
    national_bird_redlist_reference varchar(255)
)

BULK INSERT bgreport FROM "../../data/data_bgreport.csv"
WITH(FIRSTROW = 2, FIELDTERMINATOR = ",", ROWTERMINATOR = "\n", BATCHSIZE = 25000, MAXERRORS = 8);

create table birds_check_list
(
    country varchar(10),
    country_isocode varchar(10),
    speciescode varchar(10),
    speciesname varchar(30),
    sub_unit varchar(60),
    euringcode int,
    annexI varchar(10),
    season varchar(10),
    population_size_unit varchar(30),
    spa_trigger int,
    non_native int,
    presence int,
    assessment_code_EU int,
    assessment_specname_EU varchar(60),
    assessment_code_trend int,
    assessment_specname_trend varchar(155)
) 

BULK INSERT birds_check_list FROM "../../data/data_birds_check_list.csv"
WITH(FIRSTROW = 2, FIELDTERMINATOR = ",", ROWTERMINATOR = "\n", BATCHSIZE = 25000, MAXERRORS = 8);

create table birds_eu_breeding_trends
(
    assessment_code_trend int,
    assessment_specname_trend varchar(155),
    population_size_unit varchar(30),
    BrPopSizeMin int,
    BrPopSizeMax int,
    BrPopSizeMinRnd int,
    BrPopSizeMaxRnd int,
    BrPopTrdSht varchar(10),
    BrPopTrdLng varchar(10),
    BrRngSize float,
    BrRngSizeRnd int,
    BrRngTrdSht varchar(10),
    BrRngTrdLng varchar(10)
)

BULK INSERT birds_eu_breeding_trends FROM "../../data/data_birds_eu_breeding_trends.csv"
WITH(FIRSTROW = 2, FIELDTERMINATOR = ",", ROWTERMINATOR = "\n", BATCHSIZE = 25000, MAXERRORS = 8);

create table birds_eu_status
(
    assessment_code_EU int,
    assessment_specname_EU varchar(155),
    season varchar(10),
    Population_status varchar(30),
    population_size_unit varchar(30),
    PopSizeMin int,
    PopSizeMax int,
    PopSizeMinRnd int,
    PopSizeMaxRnd int,
    PopTrdSht varchar(10),
    PopTrdLng varchar(10),
    Contribution_target1 varchar(30),
    addtionnal_record int
)

BULK INSERT birds_eu_status FROM "../../data/data_birds_eu_status.csv"
WITH(FIRSTROW = 2, FIELDTERMINATOR = ",", ROWTERMINATOR = "\n", BATCHSIZE = 25000, MAXERRORS = 8);

create table birds_eu_wintering_trends
(
    assessment_code_trend int,
    assessment_specname_trend varchar(155),
    population_size_unit varchar(60),
    WiPopSizeMin int,
    WiPopSizeMax int,
    WiPopSizeMinRnd int,
    WiPopSizeMaxRnd int,
    WiPopTrdSht varchar(10),
    WiPopTrdLng varchar(10)
)


BULK INSERT birds_eu_wintering_trends FROM "../../data/data_birds_eu_wintering_trends.csv"
WITH(FIRSTROW = 2, FIELDTERMINATOR = ",", ROWTERMINATOR = "\n", BATCHSIZE = 25000, MAXERRORS = 8);

create table birds
(
    specieshash varchar(60),
    country varchar(10),
    country_isocode varchar(10),
    euringcode int,
    speciescode varchar(10),
    speciesname varchar(60),
    sub_unit varchar(60),
    alternative_speciesname varchar(30),
    common_speciesname varchar(60),
    season varchar(10),
    population_date varchar(10),
    population_size_unit varchar(10),
    population_minimum_size int,
    population_maximum_size int,
    population_type_of_estimate varchar(30),
    population_method int,
    popilation_quality int,
    population_sources varchar(255),
    population_aditional_info varchar(255),
    population_trend_period varchar(10),
    population_trend varchar(30),
    population_trend_magnitude_min float,
    population_trend_magnitude_max float,
    population_trend_method int,
    population_trend_quality int,
    population_trend_sources varchar(255),
    population_trend_long_period varchar(30),
    population_trend_long varchar(10),
    population_trend_long_magnitude_min float,
    population_trend_long_magnitude_max float,
    population_trend_long_method int,
    population_trend_long_quality int,
    population_trend_long_sources varchar(255),
    population_trend_additional_info varchar(255),
    range_period varchar(10),
    sensitive_species int,
    distribution_map int,
    aditional_distribution_map int,
    range_map int,
    range_surface_area float,
    range_method int,
    range_quality int,
    range_sources varchar(255),
    range_additional_info varchar(155),
    range_trend_period varchar(10),
    range_trend varchar(30),
    range_trend_magnitude_min float,
    range_trend_magnitude_max float,
    range_trend_method int,
    range_trend_quality int,
    range_trend_sources varchar(255),
    range_trend_long_period varchar(30),
    range_trend_long varchar(10),
    range_trend_long_magnitude_min float,
    range_trend_long_magnitude_max float,
    range_trend_long_method int,
    range_trend_long_quality int,
    range_trend_long_sources varchar(255),
    range_trend_additional_info varchar(255),
    plan varchar(10),
    national_plan_adopted int,
    measures_taken varchar(255),
    further_information varchar(255),
    spa_population_unit varchar(60),
    spa_population_min int,
    spa_population_max int,
    spa_population_method int,
    spa_population_trend varchar(10),
    use_for_statistics int

)
BULK INSERT birds FROM "../../data/data_birds.csv"
WITH(FIRSTROW = 2, FIELDTERMINATOR = ",", ROWTERMINATOR = "\n", BATCHSIZE = 25000, MAXERRORS = 8);

create table bmeasures
(
  measurehash varchar(60),
  specieshash varchar(60),
  measurecode float,
  type_legal int,
  type_administrative int,
  type_contractual int,
  type_recurrent int,
  type_oneoff int,
  rankingcode varchar(10),
  location_inside int,
  location_outside int,
  location_both int,
  broad_evaluation_maintain int,
  broad_evaluation_enhance int,
  broad_evaluation_longterm int,
  broad_evaluation_noeffect int,
  broad_evaluation_unknown int,
  broad_evaluation_notevaluated int
)

BULK INSERT bmeasures FROM "../../data/data_bmeasures.csv"
WITH(FIRSTROW = 2, FIELDTERMINATOR = ",", ROWTERMINATOR = "\n", BATCHSIZE = 25000, MAXERRORS = 8);

create table bpressures_threats
(
    pressurethreathash varchar(60),
    specieshash varchar(60),
    pressurecode varchar(30),
    rankingcode varchar(10),
    quality int,
    location int,
    sources varchar(255)
)

BULK INSERT bpressures_threats FROM "../../data/data_bpressures_threats.csv"
WITH(FIRSTROW = 2, FIELDTERMINATOR = ",", ROWTERMINATOR = "\n", BATCHSIZE = 25000, MAXERRORS = 8);

create table species_birds_maes_EU27
(
    speciesname varchar(30),
    sub_unit varchar(30),
    speciescode varchar(10),
    euringcode int,
    codeeco varchar(30),
    typeasso varchar(10),
    season varchar(10),
    region varchar(10)
)

BULK INSERT species_birds_maes_EU27 FROM "../../data/species_birds_maes_EU27.csv"
WITH(FIRSTROW = 2, FIELDTERMINATOR = ",", ROWTERMINATOR = "\n", BATCHSIZE = 25000, MAXERRORS = 8);