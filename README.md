Проект для сбора сведений из динамических списков о поступлении в ВУЗ

стэк:

1. python
2. selenium


>установи uv   
>https://docs.astral.sh/uv/getting-started/installation/


установка проекта с uv

```bash
git clone https://github.com/ChernyaevAV/Abitura.git
cd abitura
uv sync
```

запуск с uv

```bash
uv run main.py
```

после загрузки и записи файлов .csv нужно открыть файл Сводки.xlsx и на вкладке "Данные" нажать "Обновить все"