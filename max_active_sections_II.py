class ZeroGrp:
    def __init__(self, start_idx: int, length: int):
        self.start_idx = start_idx
        self.length = length

class Solution:
    def maxActiveSectionsAfterTrade(
        self, sections_: str, queries_: list[list[int]]
    ) -> list[int]:
        tot_sections = len(sections_)
        tot_ones = 0
        zero_grps = []
        last_zero_grp_id = [-1] * tot_sections

        idx, grp_id = 0, -1
    
        while idx < tot_sections:
            start_idx = idx
            while idx < tot_sections and sections_[idx] == sections_[start_idx]:
                idx += 1
            section_len = idx - start_idx
            
            
            if sections_[start_idx] == '0':
                grp_id += 1
                zero_grps.append(ZeroGrp(start_idx, section_len))
            else:
                tot_ones += section_len
                

            for section_idx in range(start_idx, idx):
                last_zero_grp_id[section_idx] = grp_id


        if not zero_grps:
            return [tot_ones] * len(queries_)

        tot_adj_pairs = max(0, len(zero_grps) - 1)
        max_log2_step = tot_adj_pairs.bit_length()
        sparse_tbl = [0] * (max(1, max_log2_step) * tot_adj_pairs)

        def calc_tbl_idx(log_step: int, pair_idx: int) -> int:
            return log_step * tot_adj_pairs + pair_idx


        if tot_adj_pairs > 0:
            for pair_idx in range(tot_adj_pairs):
                sparse_tbl[calc_tbl_idx(0, pair_idx)] = (
                    zero_grps[pair_idx].length + zero_grps[pair_idx + 1].length
                )

            for log_step in range(1, max_log2_step):
                pair_idx = 0
                while pair_idx + (1 << log_step) <= tot_adj_pairs:
                    sparse_tbl[calc_tbl_idx(log_step, pair_idx)] = max(
                        sparse_tbl[calc_tbl_idx(log_step - 1, pair_idx)],
                        sparse_tbl[calc_tbl_idx(log_step - 1, pair_idx + (1 << (log_step - 1)))]
                    )
                    pair_idx += 1


        def calc_max_adj_sum(left_idx: int, right_idx: int) -> int:
            if left_idx > right_idx:
                return 0

            rng_len = right_idx - left_idx + 1
            log_step = rng_len.bit_length() - 1

            return max(
                sparse_tbl[calc_tbl_idx(log_step, left_idx)],
                sparse_tbl[calc_tbl_idx(log_step, right_idx - (1 << log_step) + 1)]
            )

        def solve_query(query: list[int]) -> int:
            qr_start = query[0]
            qr_end = query[1]

            left_grp_id = last_zero_grp_id[qr_start]
            right_grp_id = last_zero_grp_id[qr_end]

            first_fully_enclosed_grp_id = left_grp_id + 1
            last_fully_enclosed_grp_id = right_grp_id - (
                1 if sections_[qr_end] == '0' else 0
            )


            first_partial_grp_id = -1 if left_grp_id == -1 else (
                zero_grps[left_grp_id].length - (qr_start - zero_grps[left_grp_id].start_idx)
            )
            last_partial_grp_id = -1 if right_grp_id == -1 else (
                qr_end - zero_grps[right_grp_id].start_idx + 1
            )

            max_tot_merged_zeros = 0

            if first_fully_enclosed_grp_id < last_fully_enclosed_grp_id:
                max_tot_merged_zeros = max(
                    max_tot_merged_zeros,
                    calc_max_adj_sum(first_fully_enclosed_grp_id, last_fully_enclosed_grp_id - 1)
                )

            if (sections_[qr_start] == '0' and sections_[qr_end] == '0' and 
                left_grp_id + 1 == right_grp_id):
                max_tot_merged_zeros = max(
                    max_tot_merged_zeros,
                    first_partial_grp_id + last_partial_grp_id
                )

            if (sections_[qr_start] == '0' and 
                left_grp_id + 1 < right_grp_id + (1 if sections_[qr_end] == '1' else 0)):
                max_tot_merged_zeros = max(
                    max_tot_merged_zeros,
                    first_partial_grp_id + zero_grps[left_grp_id + 1].length
                )

            if sections_[qr_end] == '0' and left_grp_id < right_grp_id - 1:
                max_tot_merged_zeros = max(
                    max_tot_merged_zeros,
                    last_partial_grp_id + zero_grps[right_grp_id - 1].length
                )

            return tot_ones + max_tot_merged_zeros


        return [solve_query(q) for q in queries_]
