<?php

namespace FluentBoards\App\Http\Controllers;

use FluentBoards\App\Models\Board;
use FluentBoards\App\Models\User;
use FluentBoards\App\Services\Helper;
use FluentBoards\App\Services\UserService;
use FluentBoards\Framework\Http\Request\Request;

class UserController extends Controller
{
    private UserService $userService;

    public function __construct(UserService $userService)
    {
        parent::__construct();
        $this->userService = $userService;
    }

    public function allFluentBoardsUsers()
    {
        return [
            'users'  => $this->userService->allFluentBoardsUsers(),
            'boards' => Board::select('id', 'title')->orderBy('title', 'ASC')->get()
        ];
    }

    public function memberAssociatedTaskUsers($user_id)
    {
        try {
            $uniqueUsers = $this->userService->memberAssociatedTaskUsers($user_id);

            return $this->sendSuccess([
                'users'                    => $uniqueUsers['uniqueUsers'],
                'userWiseBoardDesignation' => $uniqueUsers['userWiseBoardDesignation'],
            ], 200);
        } catch (\Exception $e) {
            return $this->sendError($e->getMessage(), 404);
        }
    }

    public function searchFluentBoardsUser(Request $request)
    {
        try {
            $search_input = $request->searchInput . trim('');

            $boardUsers = $this->userService->searchFluentBoardsUser($search_input);

            return $this->sendSuccess($boardUsers, 200);
        } catch (\Exception $e) {
            return $this->sendError($e->getMessage(), 404);
        }
    }

    public function searchMemberUser(Request $request, $user_id)
    {
        try {
            $search_input = $request->searchInput . trim('');
            $searchResult = $this->userService->searchMemberUser($search_input, $user_id);

            return $this->sendSuccess([
                'users' => $searchResult,
            ], 200);
        } catch (\Exception $e) {
            return $this->sendError($e->getMessage(), 404);
        }
    }

    public function getMemberAssociatedTasks(Request $request, $user_id)
    {
        $page = $request->getSafe('page');
        try {
            return $this->sendSuccess(
                $this->userService->getMemberAssociatedTasks($user_id, $page)
                , 200);
        } catch (\Exception $e) {
            return $this->sendError($e->getMessage(), 404);
        }
    }

    public function getMemberRelatedAcitivies(Request $request, $user_id)
    {
        $page = $request->getSafe('page');
        try {
            return $this->sendSuccess(
                $this->userService->getMemberRelatedAcitivies($user_id, $page)
                , 200);
        } catch (\Exception $e) {
            return $this->sendError($e->getMessage(), 404);
        }
    }

    public function getMemberInfo($user_id)
    {
        $user = User::findOrFail($user_id);

        $user = Helper::sanitizeUserCollections($user);

        return [
            'user' => $user
        ];
    }
}
