# Generated by Django 3.1.7 on 2021-09-02 21:08

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import manage.classes.filevalidator
import manage.models.show
import manage.utils.changeEpisodeFiles
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('accounts', '__first__'),
    ]

    operations = [
        migrations.CreateModel(
            name='Show',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('show_name', models.CharField(max_length=50)),
                ('description', models.TextField()),
                ('summary', models.CharField(default=0, max_length=50)),
                ('language', models.CharField(choices=[('ab', 'Abkhaz'), ('aa', 'Afar'), ('af', 'Afrikaans'), ('ak', 'Akan'), ('sq', 'Albanian'), ('am', 'Amharic'), ('ar', 'Arabic'), ('an', 'Aragonese'), ('hy', 'Armenian'), ('as', 'Assamese'), ('av', 'Avaric'), ('ae', 'Avestan'), ('ay', 'Aymara'), ('az', 'Azerbaijani'), ('bm', 'Bambara'), ('ba', 'Bashkir'), ('eu', 'Basque'), ('be', 'Belarusian'), ('bn', 'Bengali'), ('bh', 'Bihari'), ('bi', 'Bislama'), ('bs', 'Bosnian'), ('br', 'Breton'), ('bg', 'Bulgarian'), ('my', 'Burmese'), ('ca', 'Catalan; Valencian'), ('ch', 'Chamorro'), ('ce', 'Chechen'), ('ny', 'Chichewa; Chewa; Nyanja'), ('zh', 'Chinese'), ('cv', 'Chuvash'), ('kw', 'Cornish'), ('co', 'Corsican'), ('cr', 'Cree'), ('hr', 'Croatian'), ('cs', 'Czech'), ('da', 'Danish'), ('dv', 'Divehi; Maldivian;'), ('nl', 'Dutch'), ('dz', 'Dzongkha'), ('en', 'English'), ('eo', 'Esperanto'), ('et', 'Estonian'), ('ee', 'Ewe'), ('fo', 'Faroese'), ('fj', 'Fijian'), ('fi', 'Finnish'), ('fr', 'French'), ('ff', 'Fula'), ('gl', 'Galician'), ('ka', 'Georgian'), ('de', 'German'), ('el', 'Greek, Modern'), ('gn', 'Guaraní'), ('gu', 'Gujarati'), ('ht', 'Haitian'), ('ha', 'Hausa'), ('he', 'Hebrew (modern)'), ('hz', 'Herero'), ('hi', 'Hindi'), ('ho', 'Hiri Motu'), ('hu', 'Hungarian'), ('ia', 'Interlingua'), ('id', 'Indonesian'), ('ie', 'Interlingue'), ('ga', 'Irish'), ('ig', 'Igbo'), ('ik', 'Inupiaq'), ('io', 'Ido'), ('is', 'Icelandic'), ('it', 'Italian'), ('iu', 'Inuktitut'), ('ja', 'Japanese'), ('jv', 'Javanese'), ('kl', 'Kalaallisut'), ('kn', 'Kannada'), ('kr', 'Kanuri'), ('ks', 'Kashmiri'), ('kk', 'Kazakh'), ('km', 'Khmer'), ('ki', 'Kikuyu, Gikuyu'), ('rw', 'Kinyarwanda'), ('ky', 'Kirghiz, Kyrgyz'), ('kv', 'Komi'), ('kg', 'Kongo'), ('ko', 'Korean'), ('ku', 'Kurdish'), ('kj', 'Kwanyama, Kuanyama'), ('la', 'Latin'), ('lb', 'Luxembourgish'), ('lg', 'Luganda'), ('li', 'Limburgish'), ('ln', 'Lingala'), ('lo', 'Lao'), ('lt', 'Lithuanian'), ('lu', 'Luba-Katanga'), ('lv', 'Latvian'), ('gv', 'Manx'), ('mk', 'Macedonian'), ('mg', 'Malagasy'), ('ms', 'Malay'), ('ml', 'Malayalam'), ('mt', 'Maltese'), ('mi', 'Māori'), ('mr', 'Marathi (Marāṭhī)'), ('mh', 'Marshallese'), ('mn', 'Mongolian'), ('na', 'Nauru'), ('nv', 'Navajo, Navaho'), ('nb', 'Norwegian Bokmål'), ('nd', 'North Ndebele'), ('ne', 'Nepali'), ('ng', 'Ndonga'), ('nn', 'Norwegian Nynorsk'), ('no', 'Norwegian'), ('ii', 'Nuosu'), ('nr', 'South Ndebele'), ('oc', 'Occitan'), ('oj', 'Ojibwe, Ojibwa'), ('cu', 'Old Church Slavonic'), ('om', 'Oromo'), ('or', 'Oriya'), ('os', 'Ossetian, Ossetic'), ('pa', 'Panjabi, Punjabi'), ('pi', 'Pāli'), ('fa', 'Persian'), ('pl', 'Polish'), ('ps', 'Pashto, Pushto'), ('pt', 'Portuguese'), ('qu', 'Quechua'), ('rm', 'Romansh'), ('rn', 'Kirundi'), ('ro', 'Romanian, Moldavan'), ('ru', 'Russian'), ('sa', 'Sanskrit (Saṁskṛta)'), ('sc', 'Sardinian'), ('sd', 'Sindhi'), ('se', 'Northern Sami'), ('sm', 'Samoan'), ('sg', 'Sango'), ('sr', 'Serbian'), ('gd', 'Scottish Gaelic'), ('sn', 'Shona'), ('si', 'Sinhala, Sinhalese'), ('sk', 'Slovak'), ('sl', 'Slovene'), ('so', 'Somali'), ('st', 'Southern Sotho'), ('es', 'Spanish; Castilian'), ('su', 'Sundanese'), ('sw', 'Swahili'), ('ss', 'Swati'), ('sv', 'Swedish'), ('ta', 'Tamil'), ('te', 'Telugu'), ('tg', 'Tajik'), ('th', 'Thai'), ('ti', 'Tigrinya'), ('bo', 'Tibetan'), ('tk', 'Turkmen'), ('tl', 'Tagalog'), ('tn', 'Tswana'), ('to', 'Tonga'), ('tr', 'Turkish'), ('ts', 'Tsonga'), ('tt', 'Tatar'), ('tw', 'Twi'), ('ty', 'Tahitian'), ('ug', 'Uighur, Uyghur'), ('uk', 'Ukrainian'), ('ur', 'Urdu'), ('uz', 'Uzbek'), ('ve', 'Venda'), ('vi', 'Vietnamese'), ('vo', 'Volapük'), ('wa', 'Walloon'), ('cy', 'Welsh'), ('wo', 'Wolof'), ('fy', 'Western Frisian'), ('xh', 'Xhosa'), ('yi', 'Yiddish'), ('yo', 'Yoruba'), ('za', 'Zhuang, Chuang'), ('zu', 'Zulu')], max_length=150)),
                ('author', models.CharField(max_length=50)),
                ('copyright', models.CharField(max_length=50)),
                ('icon', models.ImageField(null=True, upload_to=manage.models.show.Show.change_file_name, validators=[manage.classes.filevalidator.FileValidator(content_types=('image/jpeg', 'image/png'))])),
                ('category', models.CharField(choices=[('Arts', 'Arts'), ('Books', 'Books'), ('Design', 'Design'), ('Fashion &amp; Beauty', 'Fashion & Beauty'), ('Food', 'Food'), ('Visual Arts', 'Visual Arts'), ('Performing Arts', 'Performing Arts'), ('Business', 'Business'), ('Careers', 'Careers'), ('Entrepreneurship', 'Entrepreneurship'), ('Investing', 'Investing'), ('Management', 'Management'), ('Marketing', 'Marketing'), ('Non-Profit', 'Non-Profit'), ('Comedy', 'Comedy'), ('Comedy Interviews', 'Comedy Interviews'), ('Improv', 'Improv'), ('Stand-Up', 'Stand-Up'), ('Education', 'Education'), ('Courses', 'Courses'), ('How To', 'How To'), ('Language Learning', 'Language Learning'), ('Self-Improvement', 'Self-Improvement'), ('Fiction', 'Fiction'), ('Comedy Fiction', 'Comedy Fiction'), ('Drama', 'Drama'), ('Science Fiction', 'Science Fiction'), ('Government', 'Government'), ('History', 'History'), ('Health &amp; Fitness', 'Health & Fitness'), ('Alternative Health', 'Alternative Health'), ('Fitness', 'Fitness'), ('Medicine', 'Medicine'), ('Mental Health', 'Mental Health'), ('Nutrition', 'Nutrition'), ('Sexuality', 'Sexuality'), ('Kids &amp; Family', 'Kids & Family'), ('Education for Kids', 'Education for Kids'), ('Parenting', 'Parenting'), ('Pets &amp; Animals', 'Pets & Animals'), ('Stories for Kids', 'Stories for Kids'), ('Leisure', 'Leisure'), ('Animation &amp; Manga', 'Animation & Manga'), ('Automotive', 'Automotive'), ('Aviation', 'Aviation'), ('Crafts', 'Crafts'), ('Games', 'Games'), ('Hobbies', 'Hobbies'), ('Home &amp; Garden', 'Home & Garden'), ('Video Games', 'Video Games'), ('Music', 'Music'), ('Music Commentary', 'Music Commentary'), ('Music History', 'Music History'), ('Music Interviews', 'Music Interviews'), ('News', 'News'), ('Business News', 'Business News'), ('Daily News', 'Daily News'), ('Entertainment News', 'Entertainment News'), ('News Commentary', 'News Commentary'), ('Politics', 'Politics'), ('Sports News', 'Sports News'), ('Tech News', 'Tech News'), ('Religion &amp; Spirituality', 'Religion & Spirituality'), ('Buddhism', 'Buddhism'), ('Christianity', 'Christianity'), ('Hinduism', 'Hinduism'), ('Islam', 'Islam'), ('Judaism', 'Judaism'), ('Religion', 'Religion'), ('Spirituality', 'Spirituality'), ('Science', 'Science'), ('Astronomy', 'Astronomy'), ('Chemistry', 'Chemistry'), ('Earth Sciences', 'Earth Sciences'), ('Life Sciences', 'Life Sciences'), ('Mathematics', 'Mathematics'), ('Natural Sciences', 'Natural Sciences'), ('Nature', 'Nature'), ('Physics', 'Physics'), ('Social Sciences', 'Social Sciences'), ('Society &amp; Culture', 'Society & Culture'), ('Documentary', 'Documentary'), ('Personal Journals', 'Personal Journals'), ('Philosophy', 'Philosophy'), ('Places &amp; Travel', 'Places & Travel'), ('Relationships', 'Relationships'), ('Sports', 'Sports'), ('Baseball', 'Baseball'), ('Basketball', 'Basketball'), ('Cricket', 'Cricket'), ('Fantasy Sports', 'Fantasy Sports'), ('Football', 'Football'), ('Golf', 'Golf'), ('Hockey', 'Hockey'), ('Rugby', 'Rugby'), ('Running', 'Running'), ('Soccer', 'Soccer'), ('Swimming', 'Swimming'), ('Tennis', 'Tennis'), ('Volleyball', 'Volleyball'), ('Wilderness', 'Wilderness'), ('Wrestling', 'Wrestling'), ('Technology', 'Technology'), ('True Crime', 'True Crime'), ('TV &amp; Film', 'TV & Film'), ('Film History', 'Film History'), ('Film Interviews', 'Film Interviews'), ('Film Reviews', 'Film Reviews'), ('TV Reviews', 'TV Reviews'), ('After Shows', 'After Shows')], max_length=150)),
                ('explict_rating', models.CharField(choices=[('yes', 'Yes'), ('no', 'No'), ('clean', 'Clean')], max_length=150)),
                ('premium_feed', models.BooleanField(default=False)),
                ('release_date', models.DateTimeField(auto_now=True)),
                ('show_type', models.CharField(choices=[('episodic', 'Episodic'), ('serial', 'Serial')], max_length=25)),
                ('contact_show_name', models.CharField(default='test owner', max_length=50)),
                ('contact_show_email', models.CharField(default='testowner@gmail.com', max_length=50)),
                ('facebook_username', models.CharField(blank=True, default='', max_length=32)),
                ('twitter_username', models.CharField(blank=True, default='', max_length=32)),
                ('instagram_username', models.CharField(blank=True, default='', max_length=32)),
                ('tiktok_username', models.CharField(blank=True, default='', max_length=32)),
                ('youtube_username', models.CharField(blank=True, default='', max_length=32)),
                ('reddit_username', models.CharField(blank=True, default='', max_length=32)),
                ('profile_fk', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='accounts.profile')),
            ],
        ),
        migrations.CreateModel(
            name='ShowDomains',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('show_website_name', models.CharField(max_length=150, unique=True)),
                ('show_fk', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='manage.show')),
            ],
        ),
        migrations.CreateModel(
            name='PremiumSubscriptions',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('profile_fk', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='subscribed_user', to='accounts.profile')),
                ('show_fk', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='premium_show', to='manage.show')),
            ],
        ),
        migrations.CreateModel(
            name='Episode',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=50)),
                ('description', models.TextField()),
                ('summary', models.CharField(default=0, max_length=50)),
                ('bit_size', models.CharField(max_length=50)),
                ('play_length', models.CharField(default=0, max_length=50)),
                ('explict_rating', models.CharField(choices=[('yes', 'Yes'), ('no', 'No'), ('clean', 'Clean')], max_length=150)),
                ('episode_type', models.CharField(choices=[('full', 'Full'), ('trailer', 'Trailer'), ('bonus', 'Bonus')], max_length=25)),
                ('season_number', models.IntegerField(default=0)),
                ('episode_number', models.IntegerField(default=0)),
                ('file_type', models.CharField(default='audio/mpeg', max_length=50)),
                ('release_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('published', models.BooleanField(default=False)),
                ('icon', models.ImageField(blank=True, null=True, upload_to=manage.utils.changeEpisodeFiles.change_ep_image, validators=[manage.classes.filevalidator.FileValidator(content_types=('image/jpeg', 'image/png'))])),
                ('audio', models.FileField(null=True, upload_to=manage.utils.changeEpisodeFiles.change_ep_audio, validators=[manage.classes.filevalidator.FileValidator(content_types=('audio/mpeg',))])),
                ('show_fk', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='episode_id', to='manage.show')),
            ],
        ),
    ]