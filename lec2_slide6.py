# coding: UTF-8

from naoqi import ALProxy
tts = ALProxy("ALTextToSpeech", "localhost", 9559)
tts.setLanguage("Japanese")
tts.say("知識工学は、現在のコンピューターヒューマンインタラクション研究のベースになっている学問でもあります。知識工学のエッセンスは、次の通りです。まず、知識ベースを構築するための学問、ということです。知識ベース構築では、専門家が持っている知識をコンピューターで扱える表現にしてデータベース化することが重要です。論理的に整合性のある形で知識を書くことが求められるため、いかに知識ベースを作るかを扱うのがこの学問の中心的な課題となります。そして、この知識ベースを使って、実際の問題解決を図るエキスパートのような振る舞いを実現することが知識工学の目標、となります。そのために、知識ベースを用いた問題解決を実現するための推論エンジンが開発されてきました。知識工学のAIに対する貢献は何かといいますと、知識ベースと推論エンジンを明確に分離して、システムを構築したというところにあります。AIでは、しばしば推論エンジンの中に知識を埋め込んで記述してしまっていました。これでは、システムをアップデートをするようなときに、知識自体をアップデートするのか推論エンジンの方をアップデートするのか明確に切り分けられなくて、システムの保守が難しくなります。今では、ソフトウェア工学的に種類の異なるデータを分けて記述するというのは一般的な話ですが、当時は分けずに書いていました。しかし、知識工学は、役割の異なる知識を分けて記述する必要性を明確にしました。これがAIに対する非常に大きな貢献の一つになっています。")