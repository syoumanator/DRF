from django.db import models


class Course(models.Model):
    title = models.CharField(max_length=100, verbose_name='Название курса')
    preview = models.ImageField(upload_to='education/courses/preview', blank=True, null=True)
    description = models.TextField(verbose_name='Описание курса')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Курс'
        verbose_name_plural = 'Курсы'


class Lesson(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='Уроки', verbose_name='Курс')
    title = models.CharField(max_length=100, verbose_name='Название урока')
    description = models.TextField(verbose_name='Описание урока')
    preview = models.ImageField(upload_to='education/lessons/preview', blank=True, null=True)
    video_url = models.URLField(verbose_name='Ссылка на видео')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Урок'
        verbose_name_plural = 'Уроки'
