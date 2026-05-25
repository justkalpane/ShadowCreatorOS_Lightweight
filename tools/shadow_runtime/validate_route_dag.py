from __future__ import annotations
import argparse
from common import output
from route_graph_builder import build_route


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--route", required=True)
    ap.add_argument("--dag-file")
    ap.add_argument("--lifecycle-file")
    ap.add_argument("--out")
    args = ap.parse_args()
    result = build_route(args.route, args.dag_file, args.lifecycle_file)
    output(result, args.out)
    raise SystemExit(0 if result.get("pass") else 1)


if __name__ == "__main__":
    main()
