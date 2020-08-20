#if 0
_f=$(mktemp); /usr/bin/env clang++ $(pkg-config --cflags --libs Qt5Core) -fPIC -O --std=c++2a -o $_f "$0"
chmod +x $_f; $_f "$@"; rm $_f; exit
#endif

#include <QFile>
#include <QSet>
#include <QTextStream>

QSet<QString> build_set(const char *base_file) {
    QFile f { base_file };
    f.open(QFile::ReadOnly | QFile::Text);
    QTextStream ts { &f };

    // Skip header
    while (true)
        if (const QString line = ts.readLine(); line == "...")
            break;

    // Add to set
    QSet<QString> seen;
    while (!ts.atEnd())
        if (const QString line = ts.readLine(); !line.isEmpty() && !line.startsWith('#'))
            seen.insert(line);

    f.close();
    return seen;
}

QStringList build_list(const char *compare_file) {
    QFile f { compare_file };
    f.open(QFile::ReadOnly | QFile::Text);
    QTextStream ts { &f };

    // Add to list
    QStringList curr;
    while (!ts.atEnd())
        curr.push_back(ts.readLine());

    f.close();
    return curr;
}

void write_file(const char *compare_file, const QSet<QString> &seen, const QStringList &curr) {
    QFile f { compare_file };
    f.open(QFile::WriteOnly | QFile::Text);
    QTextStream ts { &f };

    // Keep the lines which are not seen
    for (const QString &s : curr)
        if (!seen.contains(s))
            ts << s << '\n';

    f.close();
}

int main(int argc, char *argv[]) {
    if (argc != 3) {
        QTextStream err { stderr };
        err << "Remove duplicate items between two files.\n"
               "Sample usage: tools/nubfile.cpp putonghua.dict.yaml putonghua.extra.dict.yaml" << Qt::endl;
    } else {
        const char *base_file = argv[1], *compare_file = argv[2];
        const QSet<QString> seen = build_set(base_file);
        const QStringList curr = build_list(compare_file);
        write_file(compare_file, seen, curr);
    }
}
