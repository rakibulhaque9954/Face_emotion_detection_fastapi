
# 顔の感情検出（FastAPI）

Face Emotion Detectionプロジェクトへようこそ！このアプリケーションは、アップロードされた画像から顔の感情をHaar Cascadeを使用して検出し、感情予測のためのViT（Vision Transformer）モデルを組み合わせています。このモデルは、Happy、Sad、Angry、Surprised、Neutralの5つの感情クラスで訓練されています。

## ウェブサイトプレビュー
![ホームページ](https://github.com/rakibulhaque9954/Face_emotion_detection_fastapi/blob/cde903776333edd143cc5f8a15da9dd704d452e7/Screenshot%202023-11-11%20at%2018.17.25.png)
*ホームページ*
<br>
<img src="https://github.com/rakibulhaque9954/Face_emotion_detection_fastapi/blob/cde903776333edd143cc5f8a15da9dd704d452e7/1000_F_637048304_gG1q9XoPsy17wtqm1rCM8ke3EjENcq5N.jpg" width="400" alt="サンプルハッピーイメージ"><br>
*テスト画像（感情：ハッピー）*
<br>
![結果](https://github.com/rakibulhaque9954/Face_emotion_detection_fastapi/blob/cde903776333edd143cc5f8a15da9dd704d452e7/Screenshot%202023-11-11%20at%2018.18.03.png)
*結果ページ*

## 使用方法

1. 顔が含まれた画像をアップロードします。
2. Haar Cascadeアルゴリズムが顔を検出します。
3. 画像はnumpy配列に変換され、ViT Transformerモデルに渡されます。
4. モデルは検出された顔の感情を予測します。

## モデルの詳細

- 私はGoogleのPatch 16データセットで事前トレーニングされたViT Transformerモデルを使用しており、画像サイズは224x224ピクセルです。
- モデルは、感情を正確に分類するために、Kaggleのデータセットと追加のカスタムデータを含むカスタム感情データセットで微調整されています。

## カスタムデータセットとKaggleの追加

モデルの精度向上のために、Kaggleのデータセットと追加のカスタムデータを含むカスタムデータセットを追加しました。この拡張データセットにより、モデルはより幅広い範囲の感情を理解し、分類することができました。
**正解率90％を達成しました。**

## デプロイメント

このプロジェクトはRenderでホストされており、読み込み時間や安定性に影響を与える場合があります。ウェブアプリケーションの性質上、時折クラッシュが発生したり、応答時間が遅くなることがあります。

## 使用技術

- FastAPI：Webアプリケーションの構築に使用
- Haar Cascade：顔の検出に使用
- Vision Transformer（ViT）：感情の予測に使用
- GoogleのPatch 16データセット：ViTモデルの事前トレーニングに使用
- Kaggleデータセット：包括的なトレーニングに組み込まれました。

## ローカルでアプリケーションを実行

このアプリケーションをローカルで実行するには、以下の手順を実行してください：

1. このリポジトリをクローンします。
2. 必要な依存関係を `pip install -r requirements.txt` を使用してインストールします。
3. FastAPIアプリケーションを `uvicorn app:app --reload` を使用して実行します。

## ノートブックリポジトリ

プロジェクトの開発とモデルトレーニングを詳細に調べるには、ノートブックリポジトリを [こちら](https://github.com/rakibulhaque9954/Emotion_Detection_Model-ViT-_V1.0.git) から探索してください。

## 貢献

貢献は歓迎します！提案や改善点がある場合は、問題を開いたりプルリクエストを送信したりしてください。

## ライセンス

このプロジェクトはMITライセンスの下でライセンスされています - 詳細については[LICENSE](https://github.com/rakibulhaque9954/blog_remastered/blob/418d35cf33f0411375ed2dc77fc3607ee5887fc9/MIT_LICENSE_Rakibul_Haque.txt) ファイルを参照してください。

Face Emotion Detectionアプリケーションの探索と使用をお楽しみください！
