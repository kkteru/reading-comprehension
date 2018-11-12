import argparse
import os


def setup_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("--data_dir", required=True)
    parser.add_argument("--tres", required=True)
    return parser.parse_args()


def intstr_to_intlist(string):
    """Given a string e.g. '311 9 1334 635 6192 56 639', returns as a list of integers"""
    return [int(s) for s in string.split()]


def overlap_count(span_list, tres=0):
    count = 0
    for i in range(len(span_list)):
        for j in range(i):
            a = span_list[i][1] - span_list[i][0]
            b = span_list[j][1] - span_list[j][0]
            c = max(span_list[i][1], span_list[j][1]) - min(span_list[i][0], span_list[j][0])
            if (a + b - c) >= tres:
                # if (span_list[i][0] <= span_list[j][0] and span_list[j][0] <= span_list[i][1]) or (span_list[j][0] <= span_list[i][0] and span_list[i][0] <= span_list[j][1]):
                count += 1
    return count


def get_total_overlap_counts(file_name, tres=0):
    file = open(file_name)

    line = intstr_to_intlist(file.readline())

    count = 0

    while len(line):
        curr_id = line[0]
        l = []
        while len(line) != 0 and line[0] == curr_id:
            l.append([line[1], line[2]])
            line = intstr_to_intlist(file.readline())
        count += overlap_count(l, tres)

    return count


def main():
    args = setup_args()

    dev_file_name = 'dev_ind.span'
    train_file_name = 'train_ind.span'

    print 'No. of overlapping pairs in train set: ', get_total_overlap_counts(os.path.join(args.data_dir, train_file_name), int(args.tres))
    print 'No. of overlapping pairs in dev set: ', get_total_overlap_counts(os.path.join(args.data_dir, dev_file_name), int(args.tres))


if __name__ == '__main__':
    main()
