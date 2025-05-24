import 'package:flutter/material.dart';
import 'package:flutter/services.dart';
import 'package:youtube_player_flutter/youtube_player_flutter.dart';

void main() {
  runApp(const MyApp());
}

class MyApp extends StatelessWidget {
  const MyApp({super.key});

  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      title: 'Recommend App',
      debugShowCheckedModeBanner: false,
      home: const RecommendPage(),
    );
  }
}

class RecommendPage extends StatefulWidget {
  const RecommendPage({super.key});

  @override
  State<RecommendPage> createState() => _RecommendPageState();
}

class _RecommendPageState extends State<RecommendPage> {
  final Map<String, String> categoryVideos = {
    'SINDROME DOWN': 'I377CImnC-8',
    'ADHD': 'i1oHsML1kOk',
    'AUTISM': '-fYuMzA9Js8',
  };

  final Map<String, String> categoryDescriptions = {
    'SINDROME DOWN': ''
        'Title: DENTAL MANAGEMENT FOR DOWN SYNDROME\n'
        '\n'
        '1. Brush twice a day with fluoride toothpaste for 2 minutes, including your tongue.\n'
        '2. Floss daily to clean between your teeth.'
        '3. Use mouthwash once a day to kill germs and freshen breath.\n'
        '4. Eat less sugar, and more calcium-rich and crunchy foods.\n'
        '5. See a dentist every 6 months.\n',
    'ADHD': ''
        'Title: ADHD AND TOOTHBRUSHING STRUGGLES – WORKAROUND FROM A DENTIST!\n'
        '\n'
        '1. Use colorful toothbrushes or flavored toothpaste that the individual enjoys.\n'
        '2. Brush teeth in the shower or while listening to favorite music\n'
        '3. Place sticky notes in visible places or set alarms as prompts.\n'
        '4. Try using an electric toothbrush or a brushing app that times and tracks brushing\n'
        '5. Brush teeth alongside a friend or family member can boost motivation\n',
    'AUTISM': ''
        'TITLE: MODELING BRUSHING  TEETH - AUTISM\n'
        '\n'
        '1. Get a toothbrush, toothpaste, cup, and towel\n'
        '2. Stand at the sink and make sure everything is within reach\n'
        '3. Wet the bristles of the toothbrush slightly.\n'
        '4, Brush the outside of the top teeth (front, left to right).\n'
        '5. Repeat the same steps on the bottom teeth (outside front and sides).\n'
        '6. Tilt the toothbrush and brush the inside of the top and bottom teeth.\n'
        '7. Brush the tops (chewing parts) of molars on both sides.\n'
        '8. Take a cup of water, swish it around the mouth, and spit into the sink.\n'
        '9. Wash off the toothbrush under the tap and put it back in its holder.\n',
  };

  String selectedCategory = 'ADHD';
  late YoutubePlayerController _controller;

  @override
  void initState() {
    super.initState();
    _controller = YoutubePlayerController(
      initialVideoId: categoryVideos[selectedCategory]!,
      flags: const YoutubePlayerFlags(
        autoPlay: false,
        mute: false,
        controlsVisibleAtStart: true,
        forceHD: true,
        isLive: false,
      ),
    );
  }

  @override
  void dispose() {
    _controller.dispose();
    super.dispose();
  }

  void _changeCategory(String category) {
    setState(() {
      selectedCategory = category;
      _controller.load(categoryVideos[category]!);
    });
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      backgroundColor: Colors.white,
      appBar: PreferredSize(
        preferredSize: const Size.fromHeight(60),
        child: AppBar(
          automaticallyImplyLeading: false,
          flexibleSpace: Container(
            decoration: const BoxDecoration(
              gradient: LinearGradient(
                colors: [Color(0xFF1A237E), Color(0xFF3949AB)],
                begin: Alignment.topLeft,
                end: Alignment.bottomRight,
              ),
            ),
          ),
          title: const Text(
            'RECOMMEND',
            style: TextStyle(
              fontSize: 28,
              fontWeight: FontWeight.w600,
              color: Colors.white,
            ),
          ),
          centerTitle: true,
        ),
      ),
      body: SingleChildScrollView(
        child: Padding(
          padding: const EdgeInsets.all(16.0),
          child: YoutubePlayerBuilder(
            player: YoutubePlayer(
              controller: _controller,
              showVideoProgressIndicator: true,
              bottomActions: [
                CurrentPosition(),
                ProgressBar(isExpanded: true),
                PlaybackSpeedButton(),
                FullScreenButton(),
              ],
            ),
            onEnterFullScreen: () {
              SystemChrome.setPreferredOrientations([
                DeviceOrientation.landscapeLeft,
                DeviceOrientation.landscapeRight,
              ]);
            },
            onExitFullScreen: () {
              SystemChrome.setPreferredOrientations([
                DeviceOrientation.portraitUp,
              ]);
            },
            builder: (context, player) => Column(
              crossAxisAlignment: CrossAxisAlignment.start,
              children: [
                const Text(
                  'Categories',
                  style: TextStyle(
                    fontSize: 24,
                    fontWeight: FontWeight.w600,
                  ),
                ),
                const SizedBox(height: 12),
                SingleChildScrollView(
                  scrollDirection: Axis.horizontal,
                  child: Row(
                    children: categoryVideos.keys.map((category) {
                      final isSelected = selectedCategory == category;
                      return GestureDetector(
                        onTap: () => _changeCategory(category),
                        child: Container(
                          margin: const EdgeInsets.symmetric(horizontal: 8),
                          padding: const EdgeInsets.symmetric(
                              horizontal: 16, vertical: 8),
                          decoration: BoxDecoration(
                            color: isSelected
                                ? Colors.blue[300]
                                : Colors.grey[300],
                            borderRadius: BorderRadius.circular(12),
                          ),
                          child: Text(
                            category,
                            style: TextStyle(
                              fontSize: 16,
                              fontWeight: FontWeight.w600,
                              color: isSelected ? Colors.white : Colors.black,
                            ),
                          ),
                        ),
                      );
                    }).toList(),
                  ),
                ),
                const SizedBox(height: 20),
                Center(child: player),
                const SizedBox(height: 20),
                Center(
                  child: Container(
                    width: 400,
                    padding: const EdgeInsets.all(12),
                    decoration: BoxDecoration(
                      color: Colors.lightBlueAccent,
                      borderRadius: BorderRadius.circular(12),
                    ),
                    alignment: Alignment.topLeft,
                    child: Text(
                      categoryDescriptions[selectedCategory] ??
                          'No description available.',
                      style: const TextStyle(
                          fontSize: 16, fontWeight: FontWeight.w600),
                    ),
                  ),
                ),
              ],
            ),
          ),
        ),
      ),
    );
  }
}
