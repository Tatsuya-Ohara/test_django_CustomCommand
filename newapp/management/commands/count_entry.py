from django.core.management.base import BaseCommand


class Command(BaseCommand):
    help = 'テストコマンド'
    
    def handle(self, *args, **options):
        print(options['name'])
        print(f'{options["name"]} Hello, world!!')
    
    def add_arguments(self, parser):
        parser.add_argument('--name', nargs='?', default='', type=str)

# # BaseCommandを継承して作成
# class Command(BaseCommand):
#     # python manage.py help count_entryで表示されるメッセージ
#     help = 'Display the number of blog articles'

#     # コマンドライン引数を指定（argparseモジュール
#     # 今回はblog_idという名前で取得する
#     def add_arguments(self, parser):
#         # 引数の個数は1個以上（+）
#         parser.add_argument('blog_id', nargs='+', type=int)

#     # コマンドが実行された際に呼ばれるメソッド
#     def handle(self, *args, **options):
#         for blog_id in options['blog_id']:
#             articles_count = Article.objects.filter(blog_id=blog_id).count()

#             self.stdout.write(self.style.SUCCESS('Article count = "%s"' % articles_count))
