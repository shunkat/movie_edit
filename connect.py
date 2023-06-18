import os
import sys
from moviepy.editor import concatenate_videoclips, VideoFileClip


def concatenate_videos(dir_path):
    # ディレクトリ内の.mp4ファイルを名前順に取得
    mp4_files = sorted([f for f in os.listdir(dir_path) if f.endswith('.MP4')])

    # 各動画から音声を削除し、それらをリストに追加
    clips = []
    for mp4_file in mp4_files:
        clip = VideoFileClip(os.path.join(dir_path, mp4_file))
        clip = clip.without_audio()  # 音声を削除
        clips.append(clip)

    # 動画を結合
    final_clip = concatenate_videoclips(clips)

    # 結合した動画を出力
    final_clip.write_videofile(os.path.join(dir_path, 'output.mp4'))


if __name__ == "__main__":
    # コマンドライン引数からディレクトリパスを取得
    if len(sys.argv) != 2:
        print("Usage: python connect.py path_to_your_directory")
        sys.exit(1)

    dir_path = sys.argv[1]
    concatenate_videos(dir_path)
