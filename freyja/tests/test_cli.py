import unittest
import os


def file_exists(directory, filename):
    file_path = os.path.join(directory, filename)
    return os.path.exists(file_path)


class CommandLineTests(unittest.TestCase):

    def test_version(self):
        os.system('freyja --version')

    def test_demix(self):
        os.system('freyja demix freyja/data/test.tsv freyja/data/test.depth \
                   --output test.demixed.tsv')
        self.assertTrue(file_exists('.', "test.demixed.tsv"))

    def test_demix_with_cutoff(self):
        os.system('freyja demix freyja/data/test.tsv freyja/data/test.depth \
                   --output test.demixed.tsv --depthcutoff 100 --lineageyml \
                   freyja/data/lineages.yml')
        self.assertTrue(file_exists('.', "test_collapsed_lineages.yml"))

    def test_plot(self):
        os.system('freyja plot freyja/data/aggregated_result.tsv \
                   --output test_plot.pdf')
        self.assertTrue(file_exists('.', "test_plot.pdf"))

    def test_plot_time(self):
        os.system('freyja plot freyja/data/test_sweep.tsv \
                   --times freyja/data/sweep_metadata.csv \
                   --output test_plot_time.pdf \
                   --config freyja/data/plot_config.yml --lineageyml \
                   freyja/data/lineages.yml --interval D')
        self.assertTrue(file_exists('.', "test_plot_time.pdf"))

    def test_growth_rate(self):
        os.system('freyja relgrowthrate freyja/data/test_sweep.tsv \
                   freyja/data/sweep_metadata.csv \
                   --output test_growth_rates.csv \
                   --config freyja/data/plot_config.yml \
                   --lineageyml freyja/data/lineages.yml')
        self.assertTrue(file_exists('.', "test_growth_rates.csv"))

    def test_dash(self):
        os.system('freyja dash freyja/data/test_sweep.tsv \
                   freyja/data/sweep_metadata.csv \
                   freyja/data/title.txt \
                   freyja/data/introContent.txt \
                   --lineageyml freyja/data/lineages.yml \
                   --output test_dash.html')
        self.assertTrue(file_exists('.', "test_dash.html"))


if __name__ == '__main__':
    unittest.main()